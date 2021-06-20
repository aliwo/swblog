
__all__ = ['create_strategy']

from _drafts.delivery_hero_2020.q2_with_strategy_pattern.add_strategy import AddStrategy
from _drafts.delivery_hero_2020.q2_with_strategy_pattern.number_strategy import NumberStrategy

strategy_map = {
    '+': AddStrategy,
}

def create_strategy(machine, command):
    if command.is_numeric():
        return NumberStrategy(machine, command)
    return strategy_map.get(command)(machine, command)

