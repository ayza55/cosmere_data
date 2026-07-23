from characters_scraper import CharacterScraper
from infobox_scraper import InfoboxScraper
import json

charscraper = CharacterScraper()
characters = charscraper.scrape("Category:Nalthians")

infoscraper = InfoboxScraper()

info = infoscraper.scrape(characters[0])
print(info)