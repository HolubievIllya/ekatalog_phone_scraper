# Ekatalog_phone_scraper
This is a Python script for scraping phone information from the ekatalog website and storing it in a CSV file.
# Requirements
<ul>
  <li>Python 3.10</li>
  <li>BeautifulSoup4</li>
  <li>Requests</li>
  <li>Fake User Agent</li>
</ul>

# Installation
<ol type = "1">
  <li>Clone or download the repository.</li>
  <li>Install the required packages using pip: <p><b>pip install beautifulsoup4 requests fake-useragent</li></p></b>
  <li>Run the script.</li>
</ol>

# Usage
The script will scrape phone information from the website ek.ua and store it in a CSV file named with the current date in format "DD-MM-YYYY HOURS-MINUTES-SECONDS.csv". 
The CSV file will contain the following columns:
<ul>
  <li>Товар (Product)</li>
  <li>Ціна (Price)</li>
</ul>
The script will scrape all pages of the website and collect information for all phones on the website. 
The script uses fake user agent to avoid being detected as a scraper and get blocked by the website. In addition you can try scrape any product from ek.ua, just change the url.

# Contributing
If you find any issues or have any suggestions for improvement, please open an issue or submit a pull request.
