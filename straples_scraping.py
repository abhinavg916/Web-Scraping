import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = []
product_names = []
product_prices = []

for i in range(1,50):
    url_list.append("https://www.staples.com/Computer-office-desks/cat_CL210795/663ea?pn=" + str(i))

for url in url_list:
    response = requests.get(url)
    htmlContent = response.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    item_title =  (soup.find_all("a", class_="standard-type__product_title"))
    item_price = (soup.find_all("span", class_="standard-type__price"))
    for name, price in zip(item_title, item_price):
        product_names.append(name.text.strip())
        product_prices.append(price.text.strip())
        # print(name.get_text())
        # print(price.get_text())
df = pd.DataFrame({'Product_Name':product_names, 'Product_Price':product_prices}, columns=['Product_Name', 'Product_Price'])
df.to_csv('staples_data.csv')