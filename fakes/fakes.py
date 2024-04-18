from inputio.input_io import InputIO


class InputFake(InputIO):
    def __init__(self, lista):
        self.inputlist = lista
        self.outputlist = []

    def input(self, prompt):
        return self.inputlist.pop()

    def print(self, prompt):
        self.outputlist.append(prompt)