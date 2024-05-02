class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = {}
        self.nodes: dict[str, Node] = nodes

    def get_point_by_label(self, node_name):
        return self.nodes[node_name]

    def __str__(self):
        stra = ""
        for p in self.nodes:
            stra += f"{str(self.nodes[p])}\n"
        return stra

    def calc_visits_per_session(self):
        pass


class Node:
    def __init__(self, name, paths: list, destinations: dict[str, dict]):
        self.name = name
        self.paths = paths
        self.destinations = destinations

    def __str__(self):
        return f"{self.name} - Paths: {self.paths} - Destinations: {self.destinations}"

    def get_name(self):
        return self.name

    def get_paths_to_it(self):
        return self.paths

    def add_path(self, node):
        self.paths.append(node)

    def exists_destination(self, destiny_name):
        return destiny_name in self.destinations.keys()

    def add_destination(self, destiny_node, probability: float):
        destiny_name = destiny_node.get_name()
        self.destinations[destiny_name]['probability'] = probability

    def get_destiny_probability(self, node_name):
        return self.destinations[node_name]['probability']

    def calc_visits(self):
        if not self.paths:
            return 1

        visits = 0
        for n in self.paths:
            if n.get_name() == self.name:
                probability = n.get_destiny_probability(self.name)
                
            n_visits = n.calc_visits()
            probability = n.get_destiny_probability(self.name)
            visits += n_visits * probability
        return visits