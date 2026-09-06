# import sys
# print(sys.executable)
# import sys
# print(sys.path)
from general_network.network_base import NetworkBase
from chapter_analysis.appearance_data import AppearanceData
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import hvplot.networkx as hv
import hvplot.pandas
import panel as pn
from pathlib import Path

project_root = Path("main")
file_path = Path("main/chapter_analysis/data_collection_chapter/character_freq_data_general_Mistborn_I.json")

# Get the relative path
relative_path = file_path.relative_to(project_root)


class AppearanceNetwork(NetworkBase):

    def __init__(self):
        super().__init__()
        wb = AppearanceData(r"C:\Users\ayzph\PycharmProjects\Cosmere_data\main\chapter_analysis\data_collection_chapter\character_freq_data_general_Mistborn_I.json")
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
    
    if dynamic, adds edges to the network held by the instance and returns empty list
    if static, returns the list of strings representing edge pairings.
    """
    def create_edges(self, dynamic : bool, threshold = 1):
        static_links = []
        self._parse_links()
        for i in range(self.upper_row_index):
            for j in range(i + 1, self.upper_col_index):
                if self.links[i,j] >= threshold:
                    if dynamic:
                        self.network.add_edge(self.character_list[i],
                                          self.character_list[j])
                    else:
                        static_links.append((self.character_list[i], self.character_list[j]))
        return static_links


    """
    Generates network 
    """
    def create_network_dynamic(self, filename : str, threshold):
        self.add_to_network(self.character_list, None)
        self.create_edges(True)

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

    def create_network_static(self, threshold = 0, pos = None):
        static_network = nx.Graph()

    # Add relationships
        static_network.add_nodes_from(self.character_list)
        edges = self.create_edges(dynamic=False, threshold = threshold)
        static_network.add_edges_from(edges)

        # Compute a layout to position the nodes
        if not pos:
            pos = nx.spring_layout(static_network)

        # Render the layout using Matplotlib
        plt.figure(figsize=(10, 10))
        nx.draw(
            static_network,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            node_size=200,
        )
        return (static_network, pos)






##############################################################################################
wb_network = AppearanceNetwork()
start_network, pp = wb_network.create_network_static(1)
position = nx.spring_layout(start_network, seed=42) # seed ensures reproducibility

# wb_network.create_network('warbreaker_appearance_network.html')

pn.extension()
## Using hvnx
thresh = pn.widgets.DiscreteSlider(label='Discrete Slider', options=[1,2,3,4,5,6,7], value=1)

def generate_netx_plot(threshold):
    network,_  = wb_network.create_network_static(thresh.value, pos = position)
    plot = hv.draw(network, pos=position, node_color='blue', with_labels=False, width=600, height=600,)
    return plot


plot = pn.bind(generate_netx_plot, threshold=thresh)
layout = pn.Column(thresh, plot).servable()
layout.show()
layout.save("interactive_Mistborn_I_network.html", embed = True)