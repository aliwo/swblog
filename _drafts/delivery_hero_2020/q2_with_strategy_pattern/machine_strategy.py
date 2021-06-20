from abc import ABC, abstractmethod


class MachineStrategy(ABC):

    def __init__(self, machine, command):
        self.machine = machine
        self.command = command

    @abstractmethod
    def execute(self):
        pass




