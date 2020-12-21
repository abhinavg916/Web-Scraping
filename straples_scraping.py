# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty arrays to store information
url_list = []
product_names = []
product_prices = []

# Store all url to scrap
for i in range(1,51):
    url_list.append("https://www.staples.com/Computer-office-desks/cat_CL210795/663ea?pn=" + str(i))

# Loop each page to scrap product details
for url in url_list:
    response = requests.get(url)
    htmlContent = response.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    
    # Fetching product details
    item_title =  (soup.find_all("a", class_="standard-type__product_title"))
    item_price = (soup.find_all("span", class_="standard-type__price"))
    
    # Storing product details in the array
    for name, price in zip(item_title, item_price):
        product_names.append(name.text.strip())
        product_prices.append(price.text.strip())
        # print(name.get_text())
        # print(price.get_text())

# Exporting the details in CSV
df = pd.DataFrame({'Product_Name':product_names, 'Product_Price':product_prices}, columns=['Product_Name', 'Product_Price'])
df.to_csv('staples_data.csv')