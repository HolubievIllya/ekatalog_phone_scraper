import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import date
import asyncio
import aiofiles
from aiocsv import AsyncWriter


async def parse_data():
    ua = UserAgent()
    url = "https://ek.ua/ua/list/122/samsung/"
    headers = {
        "User-Agent" : ua.random,
        "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }
    cookies = {
        "holder" : "1"
        }

    today = date.today()

    async with aiofiles.open(f"{today.strftime('%d-%m-%Y')}.csv", "w", encoding="cp1251") as ex_file:
        writer = AsyncWriter(ex_file)
        await writer.writerow(["Товар", "Ціна"])
        while True:
            responce = requests.get(url=url, headers=headers, cookies=cookies)
            soup = BeautifulSoup(responce.text, features="html.parser")
            phone_div = soup.findAll("td", class_="model-short-info")
            phone_div1 = soup.findAll("div", class_="model-price-range")
            for i, j in zip(phone_div, phone_div1):
                await writer.writerow([i.find("a")["title"], j.find("a").text])
            if soup.select_one("a.select + a.ib"):
                url = "https://ek.ua" + soup.select_one("a.select + a.ib")["href"]
                print(url)
            else:
                break
async def main():
    await parse_data()

if __name__ == "__main__":
    asyncio.run(main())