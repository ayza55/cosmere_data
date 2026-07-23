from general_network.network_base import NetworkBase
from chapter_analysis.warbreaker_appearance_data_cleanup import WarbreakerAppearanceData
import numpy as np

class WarbreakerAppearanceNetwork(NetworkBase):
    THRESHOLD = 3


    def __init__(self):
        super().__init__()
        wb = WarbreakerAppearanceData()
        self.character_apps, self.character_list = wb.character_apps, wb.character_list
        self.links = np.full(((len(self.character_list)), len(self.character_list)), -1)

        self.upper_row_index = len(self.character_list) - 1
        self.upper_col_index = len(self.character_list)

    """
    Determines the number of chapters both characters appear in together
    """
    def eval_link(self, character_a : list[int], character_b : list[int]):
        num = 0
        for chapter in character_a:
            if character_b.count(chapter):
                num += 1
        return int(num)

    """
    Parse the links between each combination of characters. Only fills out upper triangular matrix.
    all other values are NaN
    """
    def _parse_links(self):


        for i in range(self.upper_row_index):
            for j in range(i + 1, self.upper_col_index):
                self.links[i, j] = int(self.eval_link(self.character_apps.get(
                    self.character_list[i]),
                    self.character_apps.get(self.character_list[j])))

    """
    Adds the edges to the network based on the character appearance data. Currently adds edge 
    if characters appear together one or more times.
    """
    def create_edges(self):
        self._parse_links()
        for i in range(self.upper_row_index):
            for j in range(i + 1, self.upper_col_index):
                if self.links[i,j] >= self.THRESHOLD:
                    self.network.add_edge(self.character_list[i],
                                          self.character_list[j])


    """
    Generates network 
    """
    def create_network(self, filename : str):
        self.add_to_network(self.character_list, None)
        self.create_edges()

        self.network.barnes_hut (
            gravity=-10000,
            central_gravity=0.3,
            spring_length=250,
            spring_strength=0.04)

        # Edge appearance
        self.network.options.edges.hoverWidth = 2.4
        self.network.options.edges.selectionWidth = 4.9
        self.network.options.edges.smooth.forceDirection = "none"

        self.network.options.physics.stabilization.enabled = True
        self.network.options.physics.stabilization.iterations = 1000

        # self.network.show_buttons(filter_ = ['edges', 'renderer'])
        self.show_network(filename)





##############################################################################################
wb_network = WarbreakerAppearanceNetwork()
wb_network.create_network('warbreaker_appearance_network.html')
