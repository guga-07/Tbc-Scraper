from bs4 import BeautifulSoup
import requests

get_data = input("გთხოვთ შეიყვანოთ ვალუტა, რომელთა მიმართებითაც გაინტერესებთ ლარის ღირებულება {USD/EURO/GBP}: ")
source = requests.get("https://www.tbcbank.ge/web/ka/web/guest/exchange-rates").text
soup = BeautifulSoup(source, 'html.parser')

scrap_values = soup.find_all("div", class_="currRateTop")
values = [tag.text.strip() for tag in scrap_values]

if get_data == "USD" or get_data == "usd":
    print(f"რეალურ დროში 1 დოლარი არის:  {values[0]} ლარი" )
else if get_data == "EURO" or get_data == "euro":
    print(f"რეალურ დროში 1 ევრო  არის:  {values[1]} ლარი" )
else if get_data == "GBP" or get_data == "gbp":
    print(f"რეალურ დროში 1 სტერლინგი არის:  {values[2]} ლარი")
else:
    print("გთხოვთ მონაცემი შეიყვანოთ სწორად")
