
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
def web_scrapper(url):
    my_url = url
    uclient = ureq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    product = page_soup.findAll("span", {"id" : "priceblock_ourprice"})
    text_1 = product[0].text
    text_1 = text_1[1:]
    text_2 = str()
    text_1 = text_1.replace(',', '')
    for i in text_1:
        if i != '.':
            text_2 = text_2 + i 
        else:
            break
    
    return(text_2)
            