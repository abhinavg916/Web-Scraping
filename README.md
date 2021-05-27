# Web Scraping using Python and BeautifulSoup

## Introduction

- Stages:

  - Setting up Environment
  - Get the HTML
  - Parse the HTML
  - HTML Tree traversal
  - Use BeautifulSoup library to scrap data
  - Save the result in `.csv` file

- Ways to scrap a website:
  - Use the API
  - Scrap the HTML using tools (like Selenium) and libraries (like BeautifulSoup)

#### Setting up Environment

- Basic Requirements:

  - Python with Environment Setup
  - VSCode with Python (Microsoft) and Jupyter extensions
  - Jupyter Notebook (Optional) (On VSCode/Browser)

- `requests` library is used to make GET and POST request on the webpage
- `html5lib` library is used to parse the HTML
- `BeautifulSoup` library is used to manage the scrap of HTML

```
pip install requests
pip install html5lib
pip install bs4
```

#### Import Libraries and the set the destination URL to scrap

```python
import json
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
```

## Get the HTML

```python
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
```

## Parse the HTML

```python
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)
print(soup.prettify) # .prettify formats the code well with proper indents
```

## HTML Tree Traversal (DOM) & Use of BeautifulSoup to scrap the HTML

#### Get the title of HTML page

```python
title = soup.title
print(title) # Prints the <title> tag on console
print(title.string) # Prints the string of the <title> on console
```

#### Commonly used types of objects in BeautifulSoup

- Tag
- NavigableString - It is different from normal string in Python because it comes with in-build special functions
- BeautifulSoup
- Comment

```python
print(type(title)) # Prints the type on console. Here, it is Tag <class 'bs4.element.Tag'>
print(type(title.string)) # Prints the type on console. Here, it is String <class 'bs4.element.NavigableString'>
print(type(soup)) # Here, it is BeautifulSoup object <class 'bs4.BeautifulSoup'>
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p) # Prints the p tag on console
print(soup2.p.string) # Prints the content of p tag on console ("this is a comment")
print(type(soup2.p.string)) # Here, it is Comment <class 'bs4.element.Comment'>
# exit() # To terminate the execution of program at any time
```

#### Get all the paragrahps from the page

```python
paras = soup.find_all('p')
print(paras)
```

#### Get all the anchors from the page

```python
anchors = soup.find_all('a')
print(anchors)
```

#### Get only the first paragraph from the page

```python
para = soup.find('p')
print(para)
```

#### Get the class of any tag from the page

```python
paraClass = (soup.find('p')['class'])
print(paraClass)
```

#### Find all the elements with class "specific-name"

```python
print(soup.find_all("p", class_="lead"))
```

#### Get the text from the tags

```python
print(soup.find('p').get_text())
```

#### Get the text from the soup (entire HTML)

```python
print(soup.get_text())
```

#### Get all the links in anchors from the page

```python
for link in anchors:
    print(link.get('href'))
```

#### To avoid the duplication and have hyperlinks in console

```python
all_links = set()
for link in anchors:
    if(link.get('href')!='#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)
```

#### To get the element by ID

```python
navbarSupportedContent = soup.find(id="navbarSupportedContent")
print(navbarSupportedContent)
```

#### To get the children and contents of the div

```python
print(navbarSupportedContent.children)
print(navbarSupportedContent.contents) # Prints all content elements/tag inside the div in form of list
for elem in navbarSupportedContent.contents: # Prints all content one by one using loops
    print(elem)
for elem in navbarSupportedContent.children: # Prints the same as contents
    print(elem)
```

- The difference between children and content
  `.contents` - A tag's children are available as a list
  `.children` - A tag's children are available as a generator
- List uses memory to store.
- For very big large webpages, `.children` is more efficient by taking less space in memory

```python
for item in navbarSupportedContent.strings:
    print(item)

for item in navbarSupportedContent.stripped_strings: # Strips the string for ease of use
    print(item)
```

#### To get the parent

```python
print(navbarSupportedContent.parent) # Immediate Parents only
print(navbarSupportedContent.parents) # Generator object is displayed that menas it can be iterated
for item in navbarSupportedContent.parents:
    # print(item)
    print(item.name)
```

#### To get the siblings

```python
print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)
```

#### Use of CSS Selectors to target the elementss

```python
elem = soup.select('#loginModal')
print(elem)
elem = soup.select('.modal-footer')
print(elem)
```

## Save the result in .csv file

- It requires Pandas library

```
pip install pandas
```

- Import the pandas into the program for storing the data into data frame and saving the data frame later into the `.csv`

## Bypass Google CAPTCHA while Scraping with Requests

#### Problem:

- Python code to request the URL:

```python
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'} #using agent to solve the blocking issue
response = requests.get('https://www.naukri.com/jobs-in-andhra-pradesh', headers=agent)
#making the request to the link
```

- Output when printing the html :

```html
<!DOCTYPE html>

<html>
  <head>
    <title>Naukri reCAPTCHA</title>
    #the title in the actual title of the URL that I am requested for
    <meta name="robots" content="noindex, nofollow" />
    <link rel="stylesheet" href="https://static.naukimg.com/s/4/101/c/common_v62.min.css" />
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
  </head>
</html>
```

#### Solution:

- Using `Google Cache` along with a `referer` prevents these captcha's (do remember not to send more than 2 requests/sec. You may get blocked:

```python
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/'}
r = requests.get("http://webcache.googleusercontent.com/search?q=cache:www.naukri.com/jobs-in-andhra-pradesh",headers=header)
```

- This gives:

```python
>>> r.content
[Squeezed 2554 lines]
```

---

## Author

- Name - Abhinav
- GitHub - [github.com/abhinavg916](https://github.com/abhinavg916)
