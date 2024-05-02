from main import get_system_demands
from fakes.fakes import InputFake


def test_get_system_demands_1():
    system_functions = ["Entry"]
    i = InputFake(["2", "1"])
    demands = get_system_demands(i, system_functions, ["CPU", "Disk"])
    assert demands == {"Entry": {"CPU": 1.0, "Disk": 2.0}}
