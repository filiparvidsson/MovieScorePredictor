
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML
import requests


def getLinks(pages, start=1):

    if(pages > 10):
        pages = 10
        print("pages = 10 instead")

    links = []
    for i in range(pages):
        url = f"https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc&count=100&start={start}&ref_=adv_nxt"
        print(url)
        # ^ Top 1000 movies on IDBM
        response = requests.get(url)
        page = response.text
        soup = BeautifulSoup(page)
        search1 = soup.find_all(class_="lister-item-index unbold text-primary")
        link_list = [i.findNext().findChildren()[0]["href"] for i in search1]
        links.extend(link_list)
        start += 100
    return links