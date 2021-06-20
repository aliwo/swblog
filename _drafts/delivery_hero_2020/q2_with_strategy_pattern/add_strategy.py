from _drafts.delivery_hero_2020.q2_with_strategy_pattern.machine_strategy import MachineStrategy


class AddStrategy(MachineStrategy):

    def execute(self):
        self.machine.append(self.machine.pop() + self.machine.pop())

