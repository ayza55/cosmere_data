from pyvis.network import Network

import json
from network_base import NetworkBase
from pathlib import Path

# INDIVIDUAL_CHARS_FILENAME = "data_collection/characters_data.json"

# get path to the data
dir_parent = Path(__file__).parent
file_path_nalthis = dir_parent.parent / "data_collection" / "characters_data.json"


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

    # function to get list of groups, dict {group: list of members}
    """
    Returns a list of group names that the characters belong to.
    """
    def make_groups(self, characters : list[dict]) -> list[str]:
        group_names = [] # list of group names (strings) for reference

        for character in characters:
            groups = character.get("Groups")

            if groups:
                for group in groups:
                    if group_names.count(group) == 0:
                        group_names.append(group)
        return group_names

    """
    Creates and adds a node for each group.
    """
    def add_group_nodes(self, group_names:list[str]):
        self.network.add_nodes(group_names)

    # function to add character nodes
    """
    Creates and adds a node for each character, as well as edges linking the character to 
    any group they are a part of.
    """
    def add_character_nodes(self, characters: list[dict]):
        # add character node
        for character in characters:
            self.network.add_node(character["Name"])
            groups = character.get("Groups")
            if groups:
                for group in groups:
                    self.network.add_edge(group, character["Name"])

    """
    Creates the network from character data
    """
    def create_network(self, file_path, filename):
        characters = self.retrieve_data(file_path)
        groups = self.make_groups(characters)
        self.add_group_nodes(groups)
        self.add_character_nodes(characters)
        self.show_network(filename)



nw = GroupNetwork()
nw.create_network(file_path_nalthis, "nalthis_network_B.html")

