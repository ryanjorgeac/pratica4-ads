from inputio.input_io import InputIO


def create_demand_matrix(system_functions: list[str]):
    resources = ["CPU", "Disk"]
    demands_sample = [["", *system_functions]]
    for r in resources:
        demand = [r]
        for f in system_functions:
            demand.append("")
        demands_sample.append(demand)
    return resources, demands_sample


def get_system_demands(io_source: InputIO, system_functions: list[str]):
    resources, demands_sample = create_demand_matrix(system_functions)
    for i in range(len(resources)):
        for element in range(1, len(demands_sample[0])):
            usage = io_source.input(f"{resources[i]} usage: ")
            demands_sample[i][element] = usage
    return demands_sample


def get_system_functions(io_source: InputIO, system_functions: list[str]):
    print("Insert all the functions of your system by name.")
    print("When you finish, type 0 to end.")

    function = io_source.input("\n")
    while function != "0":
        system_functions.append(function)
        function = io_source.input("")
    return system_functions


def main(io_source: InputIO):
    io_source.print("Welcome to the calculator for "
                    "Systems Performances Analysis about"
                    " `Customer Behaviour Model`."
                    )

    system_functions = get_system_functions(io_source, [])
    demands = get_system_demands(io_source, system_functions)


if __name__ == "__main__":
    io = InputIO()
    main(io)
