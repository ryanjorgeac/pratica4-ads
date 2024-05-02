from graph import Graph, Node
from inputio.input_io import InputIO


def get_system_demands(io_source: InputIO, system_functions: list[str], resources: list[str]):
    demands = {}
    for f in system_functions:
        demands[f] = {}
        for r in resources:
            usage = io_source.input(f"{f} - {r} usage: ")
            demands[f][r] = float(usage)
    return demands


def get_system_functions(io_source: InputIO):
    print("Insert all the functions of your system by name.")
    print("When you finish, type 0 to end.")

    system_functions = []
    function = io_source.input("\n")
    while function != "0":
        system_functions.append(function)
        function = io_source.input("")
    return system_functions


def treat_graph_value(value: str):
    split_value = value.split(" ")
    origin = split_value[0].upper()
    destiny = split_value[2].upper()
    probability = float(split_value[4])
    return origin, destiny, probability


def get_system_graph(io_source: InputIO):
    io_source.print("Insert the graph values, such as origin, destination and probability using the following pattern: "
                    "Origin -> Destiny = 1.0"
                    "\nIt will be done when you type '0'."
                    )
    graph = Graph()
    graph_value = io_source.input(">")
    while graph_value != "0":
        origin, destiny, probability = treat_graph_value(graph_value)

        if origin in graph.nodes.keys():
            origin_node = graph.nodes[origin]
        else:
            origin_node = Node(origin, [], {})

        if destiny in graph.nodes.keys():
            destiny_node = graph.nodes[destiny]
        else:
            destiny_node = Node(destiny, [], {})

        origin_node.add_destination(destiny_node, probability)
        destiny_node.add_path(origin_node)

        graph.nodes[destiny] = destiny_node
        graph.nodes[origin] = origin_node

        graph_value = io_source.input("> ")
    return graph


def main(io_source: InputIO):
    io_source.print("Welcome to the calculator for "
                    "Systems Performances Analysis about"
                    " `Customer Behaviour Model`."
                    )

    # system_functions = get_system_functions(io_source)
    # demands = get_system_demands(io_source, system_functions, ['CPU', "Disk"])
    # print(demands, "\n")
    graph = get_system_graph(io_source)
    io_source.print(str(graph))


if __name__ == "__main__":
    io = InputIO()
    main(io)
