from src.Display.Input import Input
from random import randint
from src.DataSource.WriteToFile import WriteToFile

class InputRandom(Input):

    write_to_file = True
    input_write_to_file = WriteToFile("computerInputLog.csv")

    def get_input_string(self, request):
        return self.get_input_int()

    def get_input_int(self, request):
        rand = randint(0, 2)
        if self.write_to_file:
            self.input_write_to_file.write_to_file(rand)
        return rand
