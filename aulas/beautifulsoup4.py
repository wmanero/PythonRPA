from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

html_lib = urlopen("https://quotes.toscrape.com/")

html_req = requests.get("https://quotes.toscrape.com/")

#print(html_req.text)

soup = BeautifulSoup(html_lib.read(), "html.parser")

print(soup.h1.text)
print(soup.find(class_="text"))
print(soup.find(class_="text").attrs)

print(soup.find("span", {"itemprop": "text"}))

print(soup.find(text="deep-thoughts"))

div = soup.find("div", {"class": "quote"})

print(div.attrs) 

print(div.get("itemtype"))





