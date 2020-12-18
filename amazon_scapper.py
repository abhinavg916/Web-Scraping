from requests_html import HTMLSession
import pandas as pd

urls = ['https://www.amazon.in/Samsung-Inches-Wondertainment-UA32T4340AKXXL-Glossy/dp/B086WZSK4F/ref=sr_1_4?dchild=1&keywords=tv&qid=1608292662&sr=8-4',
          'https://www.amazon.in/Mi-inches-Ready-Android-Black/dp/B084872DQY/ref=sr_1_3?dchild=1&keywords=tv&qid=1608293137&sr=8-3',
          'https://www.amazon.in/LG-inches-Smart-43LM5650PTA-Ceramic/dp/B08G21VNQQ/ref=sr_1_15?dchild=1&keywords=tv&qid=1608292662&sr=8-15']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(timeout=20)
    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
        }
        print(product)
    except:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': 'item unavailable'
        }
        print(product)
    return product

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))

pricesdf = pd.DataFrame(tvprices)
pricesdf.to_excel('tvprices.xlsx', index=False)