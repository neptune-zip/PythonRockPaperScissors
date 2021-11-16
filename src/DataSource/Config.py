from abc import ABC, abstractmethod

class Config(ABC):

    @abstractmethod
    def get_config(self):
        pass
