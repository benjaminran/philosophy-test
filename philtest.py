#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

WIK_BASE_URL = "http://en.wikipedia.org/wiki"
WIK_RANDOM_URL = "http://en.wikipedia.org/wiki/Special:Random"

def getRandomUrl():
    return requests.get(WIK_RANDOM_URL).url

def countfrompage( url ):
    __countfrompage( url, 0 )

def __countfrompage( url, count ):
    print("Url: " + str(url) + "; Count: " + str(count))
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    print(soup)
    href = soup.find("div", {"id": "mw-content-text"}).find_next("p").find_next("a").get("href")
    if "http://" not in href:
        href = WIK_BASE_URL + href
    return __countfrompage(href, count+1)

print(countfrompage("http://en.wikipedia.org/wiki/Philosophy"))
print("From random page: " + str(countfrompage(WIK_RANDOM_URL)))
