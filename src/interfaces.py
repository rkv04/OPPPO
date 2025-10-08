from abc import ABC, abstractmethod


class OutputInterface(ABC):
    @abstractmethod
    def write(self, data):
        pass


class StorageInterface(ABC):
    @abstractmethod
    def push_back(item):
        pass

    @abstractmethod
    def get_all():
        pass