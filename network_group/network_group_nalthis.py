from pyvis.network import Network

import json
from network_base import NetworkBase
from pathlib import Path

# INDIVIDUAL_CHARS_FILENAME = "data_collection/characters_data.json"

# get path to the data
dir_parent = Path(__file__).parent
file_path = dir_parent.parent / "data_collection" / "characters_data.json"


class GroupNetwork(NetworkBase):
    """
    returns a list of dictionaries representing individual characters
    """
    def retrieve_data(self):
        with open(file_path, 'r') as file:
            characters = json.load(file)
            print(type(characters))
            print(repr(characters[:100]))
            print(type(characters[0]))
        return characters

    # function to get list of groups, dict {group: list of members}
    def make_groups(self, characters : list[dict]) -> list[dict]:
        groups = [] # list of dicts
        group_names = [] # list of group names (strings) for reference

        for character in characters:
            group = character.get("Groups")
            if group:
                if group_names.count(group) == 0:
                    groups.append({group: [character.get("Name")]})
                    group_names.append(group)
                else:
                    existing_group = [group for x in groups if x.keys() == [group]]
                    existing_group[0][group].append(character.get("Name"))
        return groups



    # function to add group nodes

    # function to add character nodes

nw = GroupNetwork()
chars = nw.retrieve_data()
print(nw.make_groups(chars))