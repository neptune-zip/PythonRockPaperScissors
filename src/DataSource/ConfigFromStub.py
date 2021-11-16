from src.DataSource.Config import Config

class ConfigFromStub(Config):

    def get_config(self):
        property_data = []
        property_data.append("Name, First, Second, Third")
        property_data.append("Rock Paper Scissors:Rock, Scissors, Paper")
        property_data.append("Star Wars:Darth Vadar, Emperor, Luke Skywalker")
        return property_data
