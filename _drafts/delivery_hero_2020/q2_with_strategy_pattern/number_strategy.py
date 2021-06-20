from _drafts.delivery_hero_2020.q2_with_strategy_pattern.machine_strategy import MachineStrategy


class NumberStrategy(MachineStrategy):

    def execute(self):
        self.machine.append(int(self.command))

