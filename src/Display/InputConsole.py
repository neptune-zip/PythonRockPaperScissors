from src.Display.Input import Input
from src.DataSource.WriteToFile import WriteToFile

class InputConsole(Input):

    write_to_file = True
    user_input_write_to_file = WriteToFile("userInputLog.csv")

    def get_input_string(self, request):
        user_input = input(request)
        if self.write_to_file:
            self.user_input_write_to_file.write_to_file(user_input)
        return user_input
