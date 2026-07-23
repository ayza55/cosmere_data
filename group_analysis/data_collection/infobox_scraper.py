from general_network.scraper import Scraper

class InfoboxScraper(Scraper):
    REMOVE = ["(", "[" ]

    """
    Returns text representation of character

    page: the name of the character
    """
    def scrape(self, page:str):
        character_base = {"Name" : page}

        request = Scraper._get_request(page)
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
                    value = Scraper.clean_data(value.split(","))
                    character_base[key] = value
        return character_base









