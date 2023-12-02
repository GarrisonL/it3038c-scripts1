import requests
from bs4 import BeautifulSoup

def scrape_yahoo_finance_news(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        #News headline extraction
        headlines = soup.find_all('h3' , class_='Mb(5px)')

        #prints the headlines
        for headline in headlines: 
            print(f"HEaDLiNe: {headline.text}\n")

    else:
        print(f"Error: Unable to fetch data. Error code: {response.error.code}")

if __name__ == "__main__":
    scrape_yahoo_finance_news('https://finance.yahoo.com/')