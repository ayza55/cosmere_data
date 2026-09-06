from pathlib import Path
import json

class AppearanceData():

    def __init__(self, path):
        self.path = path
        self.character_apps, self.character_list = self.retrieve_data(self.path)

    """
    Returns the list of lists of character appearances per chapter
    """
    def retrieve_data(self, file_path):
        with open(file_path, 'r') as file:
            appearance_data = json.load(file)

            # convert into a list of arrays, of chapter numbers per character. (chapter numbers not accurate)
            character_apps = {}
            character_list = []

            for i in range(len(appearance_data)):
                for character in appearance_data[i]:
                    appearances = character_apps.get(character)
                    if appearances:
                        character_apps[character] = appearances + [i]
                    else:
                        character_apps[character] = [i]
                        character_list.append(character)
        return character_apps, character_list

################################################################################################


