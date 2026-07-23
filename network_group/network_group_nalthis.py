from pyvis.network import Network

import json
from network_base import NetworkBase
from pathlib import Path

# INDIVIDUAL_CHARS_FILENAME = "data_collection/characters_data.json"

# get path to the data
dir_parent = Path(__file__).parent
file_path_nalthis = dir_parent.parent / "data_collection" / "characters_data.json"

# link factors
LINKS = ["Abilities", "Groups"]


class GroupNetwork(NetworkBase):

    def __init__(self):
        super().__init__()

    """
    returns a list of dictionaries representing individual characters
    """
    def retrieve_data(self, file_path):
        with open(file_path, 'r') as file:
            characters = json.load(file)
            print(type(characters))
            print(repr(characters[:100]))
            print(type(characters[0]))
        return characters

    """
    Returns list of specific categories from the main category provided.
    """
    def _get_category_nodes(self, characters : list[dict], category : str) -> list[str]:
        category_names = []
        for character in characters:
            links = character.get(category)
            if links:
                for link in links:
                    if category_names.count(link) == 0:
                        category_names.append(link)
        return category_names

    """
    From the main categories provided, finds and adds all subcategory nodes to the network.
    """
    def add_all_category_nodes(self, categories : list[str], characters : list[dict]):
        for category in categories:
            category_names = self._get_category_nodes(characters, category)
            self.add_to_network(category_names, 'red')


    """
    Searches for the category in the character dictionary, and adds edges if found
    Requires that the category results are already nodes in the system
    """
    def _add_links(self, character : dict, category : str):
        links = character.get(category)
        if links:
            for link in links:
                self.network.add_edge(link, character["Name"])

    """
    Creates and adds a node for each character, as well as edges linking the character to 
    any group they are a part of, for each given category
    """
    def _add_character_nodes(self, characters: list[dict], categories : list[str]):
        # add character node
        for character in characters:
            self.network.add_node(character["Name"])

            for category in categories:
                self._add_links(character, category)

    """
    Creates the network from character data
    """
    def create_network(self, file_path, filename):
        characters = self.retrieve_data(file_path)
        self.add_all_category_nodes(LINKS, characters)
        self._add_character_nodes(characters, LINKS)
        self.show_network(filename)



nw = GroupNetwork()
nw.create_network(file_path_nalthis, "nalthis_network_B.html")

