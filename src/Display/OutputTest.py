from src.Display.Output import Output

class OutputTest(Output):

    outputlist = []

    def set_output_list(self, output_list):
        self.outputlist = output_list

    def print(self, request):
        self.outputlist.append(request)
