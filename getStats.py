import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://books.toscrape.com"
page = requests.get(URL)

print(page.text)