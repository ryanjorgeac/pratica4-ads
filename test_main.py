from main import create_demand_matrix, get_system_demands
from fakes.fakes import InputFake


def test_create_demand_matrix():
    system_functions = ["Entry"]
    demands = create_demand_matrix(system_functions)
    assert demands == [["", "Entry"],
                       ["CPU", ""],
                       ["Disk", ""]
                       ]


def test_get_system_demands_1():
    system_functions = ["Entry"]
    i = InputFake(["2", "1"])
    demands = get_system_demands(i, system_functions)
    assert demands == [["", "Entry"],
                       ["CPU", "1"],
                       ["Disk", "2"]
                       ]
