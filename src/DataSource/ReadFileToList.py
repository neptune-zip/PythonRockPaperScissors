from src.DataSource.RockConstants import RockConstants
class ReadFileToList:

    file_path = RockConstants.file_prefix + "log/"

    def get_file_rows(self, file_name):
        file = open(self.file_path + file_name, "r")
        file_rows = file.read().splitlines()
        file.close()
        return file_rows

    def get_list(self, file_name):
        file_rows = self.get_file_rows(file_name)
        file_list = []
        for file_row in file_rows:
            if len(file_row) > 0:
                file_list.append(file_row)
        return file_list
