import requests
from general_network.scraper import Scraper

EXCLUDE = "Category"

class CharacterScraper(Scraper):

    @staticmethod
    def _get_request(page: str):
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
    def scrape(self, page:str):
        characters = []
        request = CharacterScraper._get_request(page)
        data = request.json()
        for member in data["query"]["categorymembers"]:
            title = (member["title"])
            if not(EXCLUDE in title):
                characters.append(title)
        return characters









