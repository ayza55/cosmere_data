from pyvis.network import Network

"""
General class that represents a network
"""
class NetworkBase:

    """
    Instantiate the network object held by NetworkBase
    """
    def __init__(self):
        self.network = Network()

    """
    Creates a node for each entry in data. 
    Requires data have unique entries, that are either strings or integers.
    Requires data is not null.
    """
    def add_to_network(self, data:list, colour : str):
        self.network.add_nodes(data, color = [colour] * len(data))

    """
    creates html file with filename to show the network
    """
    def show_network(self, filename: str):
        self.network.show(filename, notebook=False)
