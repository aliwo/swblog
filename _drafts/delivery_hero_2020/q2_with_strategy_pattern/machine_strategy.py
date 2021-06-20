from abc import ABC, abstractmethod


class MachineStrategy(ABC):

    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def execute(self):
        pass




