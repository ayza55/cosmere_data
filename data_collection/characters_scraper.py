from bs4 import BeautifulSoup
import requests
from scraper import Scraper

EXCLUDE = "Category"

class CharacterScraper(Scraper):

    @staticmethod
    def get_request(page: str):
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": page,
            "cmlimit": "max",
            "format": "json"
        }
        # call the request
        r = requests.get(Scraper.url, params=params)
        return r


    """
    Returns text representation of character
    """
    def scrape(self, request, **kwargs):
        characters = []
        data = request.json()
        for member in data["query"]["categorymembers"]:
            title = (member["title"])
            if not(EXCLUDE in title):
                characters.append(title)
        return characters


charscraper = CharacterScraper()
req = charscraper.get_request("Category:Nalthians")
characters = charscraper.scrape(req)
print(characters)







