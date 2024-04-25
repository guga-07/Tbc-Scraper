from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.tbcbank.ge/web/ka/web/guest/exchange-rates").text
soup = BeautifulSoup(source, 'html.parser')

scrap_values = soup.find_all("div", class_="currRateTop")
values = [tag.text.strip() for tag in scrap_values]

print(f"რეალურ დროში 1 დოლარი არის:  {values[0]} ლარი" )
print(f"რეალურ დროში 1 ევრო  არის:  {values[1]} ლარი")
print(f"რეალურ დროში 1 სტერლინგი არის:  {values[2]} ლარი")