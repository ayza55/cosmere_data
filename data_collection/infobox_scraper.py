
from bs4 import BeautifulSoup
from scraper import Scraper

class InfoboxScraper(Scraper):

    """
    Returns text representation of character
    """
    def scrape(self, request, **kwargs):
        character = kwargs.get("character")
        character_base = {"Name" : character}

        infobox = request.find("table")
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
        return str(character_base)






