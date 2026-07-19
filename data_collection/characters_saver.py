import json
from characters_scraper import CharacterScraper
from infobox_scraper import InfoboxScraper

CHAR_FILENAME = "characters_list.json"
INDIVIDUAL_CHARS_FILENAME = "characters_data.json"

# save Nalthians data first
charscraper = CharacterScraper()
characters = charscraper.scrape("Category:Nalthians")

with open(CHAR_FILENAME, "w") as file:
	json.dump(characters ,file)

# Get individual character data from the list
"""
Generates a list of dictionaries representing individual characters
"""
def get_chars(characters: list[str]) -> list[dict]:
	character_info = []
	infoscraper = InfoboxScraper()

	for character in characters:
		character_info.append(infoscraper.scrape(character))
	return character_info


nalthians_characters = get_chars(characters)
with open(INDIVIDUAL_CHARS_FILENAME, "w") as characters_file:
	json.dump(nalthians_characters, characters_file)







