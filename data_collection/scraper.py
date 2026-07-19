from bs4 import BeautifulSoup
import requests

class Scraper:
    url = "https://coppermind.net/w/api.php"

    @staticmethod
    def get_request(page: str):

        params = {
            "action": "parse",
            "page": page,
            "prop": "text",
            "format": "json"
        }

        # call the request
        r = requests.get(Scraper.url, params=params)
        html = r.json()["parse"]["text"]["*"]
        soup = BeautifulSoup(html, "html.parser")
        return soup

    """
    Return text representation of the request
    """
    def scrape(self, page: str):
        request = Scraper.get_request(page)
        return request.text




