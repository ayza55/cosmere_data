from infobox_scraper import scraper
import lxml
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

# access the api
url = "https://coppermind.net/w/api.php"
name = "Vin"
sazed_dict = {"Name": name}

scraper(url, name, sazed_dict)

print(sazed_dict)



