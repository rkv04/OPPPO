from abc import ABC, abstractmethod


class OutputInterface(ABC):
    @abstractmethod
    def write(self, data):
        pass