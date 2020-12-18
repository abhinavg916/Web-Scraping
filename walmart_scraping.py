import requests
from bs4 import BeautifulSoup as soup

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

html = requests.get('https://www.walmart.com/browse/electronics/gaming-laptops/3944_3951_1089430_1230091_1094888?cat_id=3944_3951_1089430_1230091_1094888_4519159&page=1', headers=header)
bsobj = soup(html.content, 'lxml')

bsobj

url_list = []

for i in range(1,6):
  url_list.append('https://www.walmart.com/browse/electronics/gaming-laptops/3944_3951_1089430_1230091_1094888?cat_id=3944_3951_1089430_1230091_1094888_4519159&page=' + str(i))

item_names = []
price_list = []

bsobj.findAll('div',{'class': 'search-result-product-title gridview'})
bsobj.findAll('span', {'class': 'price display-inline-block arrange-fit price price-main'})[0].findAll('span', {'class':'visuallyhidden'})[0].text

for url in url_list:
  result = requests.get(url)
  bsobj = soup(result.content,'lxml')
  product_name = bsobj.findAll('div',{'class':'search-result-product-title gridview'})
  product_price = bsobj.findAll('span',{'class':'price display-inline-block arrange-fit price price-main'})
  for names,price in zip(product_name,product_price):
    item_names.append(names.a.span.text.strip())
    price_list.append(price.findAll('span',{'class':'visuallyhidden'})[0].text)

import pandas as pd
df = pd.DataFrame({'Product_Name':item_names, 'Price':price_list}, columns=['Product_Name', 'Price'])
df.head()


