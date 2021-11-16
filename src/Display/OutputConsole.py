from src.Display.Output import Output
from src.DataSource.WriteToFile import WriteToFile

class OutputConsole(Output):

    write_to_file = True
    output_write_to_file = WriteToFile("user_output_log.csv")

    def print(self, output):
        if self.write_to_file:
            self.output_write_to_file.write_to_file(output)
        print(output)
