from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def push_back(item):
        pass

    @abstractmethod
    def get_all():
        pass