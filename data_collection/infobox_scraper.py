
from bs4 import BeautifulSoup
from scraper import Scraper

class InfoboxScraper(Scraper):
    REMOVE = ["(", "[" ]

    """
    Returns text representation of character

    page: the name of the character
    """
    def scrape(self, page:str):
        character_base = {"Name" : page}

        request = Scraper.get_request(page)
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

                    # make into list
                    value = self.clean_data(value.split(","))
                    character_base[key] = value
        return character_base

    """
    data is a list of strings.
    """
    def clean_data(self, data) -> list[str]:
        clean_data = []
        for entry in data:
            entry = entry.strip()
            for i in range(0, len(self.REMOVE)):
                index = entry.find(self.REMOVE[i])
                if index != -1:
                    entry = entry[:index]
            clean_data.append(entry.strip())
        return clean_data







