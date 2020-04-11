# Class to store information pertaining to a node
class Node:
    def __init__(self, node_data, parent_data, total_cost, base_cost, intermediate_nodes):
        """
        Initialize the node using its data, parent, and sub-nodes between node and its parent
        :param node_data: a list containing node coordinates and its orientation
        :param parent_data: all the information of the parent node object
        :param intermediate_nodes: a list of all the nodes between current node and its parent
                                    only contains coordinates and orientation in each element
        :return: nothing
        """
        self.data = node_data
        self.parent = parent_data
        self.sub_nodes = intermediate_nodes
        self.weight = total_cost
        self.base_weight = base_cost

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def get_data(self):
        """
        :return: a list containing coordinates and orientation of the node
        """
        return self.data

    def get_parent(self):
        """
        :return: parent node
        """
        return self.parent

    def get_sub_nodes(self):
        """
        :return: a list of all the nodes between current node and its parent
        """
        return self.sub_nodes

    def set_weight(self, node_weight):
        self.weight = node_weight

    def set_base_weight(self, base_cost):
        self.base_weight = base_cost
