from src.DataSource.RockConstants import RockConstants
class WriteToFile:
    # Here will be the instance stored.
    file = ""
    file_path = RockConstants.file_prefix + "log/"
    file_name = "input_log.csv"

    def __init__(self, file_name):
        self.file_name = file_name


    def write_to_file(self, log_item):
        if self.file == "":
            self.file = open(self.file_path + self.file_name, "w")
        self.file.write(str(log_item) + "\n")
