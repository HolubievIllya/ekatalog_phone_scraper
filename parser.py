import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
import csv

def parse_data():
    ua = UserAgent()
    # url can be https://ek.ua/ua/list/122/samsung/
    url = "YOUR LINK"
    headers = {
        "User-Agent" : ua.random,
        "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }
    cookies = {
        "holder" : "1"
        }

    now = datetime.now()

    with open(f"{now.strftime('%d-%m-%Y %H-%M-%S')}.csv", "w", encoding="cp1251") as ex_file:
        writer = csv.writer(ex_file)
        writer.writerow(["Товар", "Ціна"])
        while True:
            responce = requests.get(url=url, headers=headers, cookies=cookies)
            soup = BeautifulSoup(responce.text, features="html.parser")
            phone_div = soup.findAll("td", class_="model-short-info")
            phone_div1 = soup.findAll("div", class_="model-price-range")
            for i, j in zip(phone_div, phone_div1):
                writer.writerow([i.find("a")["title"], j.find("a").text])
            if soup.select_one("a.select + a.ib"):
                url = "https://ek.ua" + soup.select_one("a.select + a.ib")["href"]
            else:
                break
def main():
    parse_data()

if __name__ == "__main__":
    main()