from characters_scraper import CharacterScraper
from infobox_scraper import InfoboxScraper

charscraper = CharacterScraper()
req = charscraper.get_request("Category:Nalthians")
characters = charscraper.scrape(req)

infoscraper = InfoboxScraper()

info = infoscraper.scrape(infoscraper.get_request(characters[0],), character = characters[0])
print(info)