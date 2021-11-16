from src.Display.Input import Input

class InputTest(Input):

    input_list = []

    def get_input_string(self, request):
        return self.input_list.pop(0)

