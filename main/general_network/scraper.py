from bs4 import BeautifulSoup
import requests
import json

REMOVE = ["(", "[" ]

class Scraper:
    url = "https://coppermind.net/w/api.php"

    @staticmethod
    def _get_request(page: str):

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
        request = Scraper._get_request(page)
        return request.text

    """
    data is a list of strings.
    """
    def clean_data(self, data) -> list[str]:
        clean_data = []
        for entry in data:
            entry = entry.strip()
            for i in range(0, len(REMOVE)):
                index = entry.find(REMOVE[i])
                if index != -1:
                    entry = entry[:index]
            clean_data.append(entry.strip())
        return clean_data

    """
    Saves given data as json in the given location
    """
    def save_data(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f)


    def search_and_save(self, page : str, filename : str):
        self.save_data(self.scrape(page), filename)


