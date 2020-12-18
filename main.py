# Step 0: Import Libraries and the set the destination URL to scrap
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)
print(soup.prettify) # .prettify formats the code well with proper indents

# Step 3: HTML Tree traversal (DOM)
# Get the title of HTML page
title = soup.title
print(title) # Prints the <title> tag on console
print(title.string) # Prints the string of the <title> on console

# Commonly used types of objects in BeautifulSoup library
print(type(title)) # Prints the type on console. Here, it is Tag <class 'bs4.element.Tag'>
print(type(title.string)) # Prints the type on console. Here, it is String <class 'bs4.element.NavigableString'>
print(type(soup)) # Here, it is BeautifulSoup object <class 'bs4.BeautifulSoup'>
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p) # Prints the p tag on console
print(soup2.p.string) # Prints the content of p tag on console ("this is a comment")
print(type(soup2.p.string)) # Here, it is Comment <class 'bs4.element.Comment'>
# exit() # To terminate the execution of program at any time

# Get all the paragrahps from the page
paras = soup.find_all('p')
print(paras)

# Get all the anchors from the page
anchors = soup.find_all('a')
print(anchors)

# Get only the first paragraph from the page
para = soup.find('p')
print(para)

# Get the class of any tag from the page
paraClass = (soup.find('p')['class'])
print(paraClass)

# Find all the elements with class "specific-name"
print(soup.find_all("p", class_="lead"))

# Get the text from the tags
print(soup.find('p').get_text())

# Get the text from the soup (entire HTML)
print(soup.get_text())

# Get all the links in anchors from the page
for link in anchors:
    print(link.get('href'))

# To avoid the duplication and have hyperlinks in console
all_links = set()
for link in anchors:
    if(link.get('href')!='#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

# To get the element by ID
navbarSupportedContent = soup.find(id="navbarSupportedContent")
print(navbarSupportedContent)

# To get the children and contents of the div
print(navbarSupportedContent.children)
print(navbarSupportedContent.contents) # Prints all content elements/tag inside the div in form of list
for elem in navbarSupportedContent.contents: # Prints all content one by one using loops
    print(elem)
for elem in navbarSupportedContent.children: # Prints the same as contents
    print(elem)
# The difference between children and content
# `.contents` - A tag's children are available as a list
# `.children` - A tag's children are available as a generator
# List uses memory to store.
# For very big large webpages, `.children` is more efficient by taking less space in memory

for item in navbarSupportedContent.strings:
    print(item)

for item in navbarSupportedContent.stripped_strings: # Strips the string for ease of use
    print(item)

# To get the parent
print(navbarSupportedContent.parent) # Immediate Parents only
print(navbarSupportedContent.parents) # Generator object is displayed that menas it can be iterated
for item in navbarSupportedContent.parents:
    # print(item)
    print(item.name)

# To get the sibling
print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

# Use of CSS Selectors to target the elementss
elem = soup.select('#loginModal')
print(elem)
elem = soup.select('.modal-footer')
print(elem)