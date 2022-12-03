from abc import ABC, abstractmethod


class Queue(ABC):

    @abstractmethod
    def insert(self, server, queue, message):
        pass

    @abstractmethod
    def remove(self, server, queue):
        pass
