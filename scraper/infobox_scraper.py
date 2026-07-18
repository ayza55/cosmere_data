import lxml
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

def scraper(url : str,
            character : str,
            character_base : dict):

    # tell api to access character page
    params = {
        "action": "parse",
        "page": character,
        "prop": "text",
        "format": "json"
    }

    # call the request
    r = requests.get(url, params=params)
    html = r.json()["parse"]["text"]["*"]

    soup = bs(html, "html.parser")
    infobox = soup.find("table")

    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            cells = row.find_all(["th", "td"])
            if len(cells) == 1:
                key = cells[0].get_text().strip()
                value = None
            elif len(cells) == 2:
                key = cells[0].get_text().strip()
                value = cells[1].get_text().strip()
                character_base[key] = value







