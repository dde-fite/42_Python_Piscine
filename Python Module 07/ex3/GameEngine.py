from typing import Any
from random import randrange
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.stats: dict[str, Any] = {
            'turns_simulated': 0,
            'strategy_used': None,
            'total_damage': 0,
            'cards_created': 0
        }

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy
                         ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.stats['strategy_used'] = strategy.get_strategy_name()
        print(f"Factory: {type(factory).__name__}\n"
              f"Strategy {type(strategy).__name__}")

    def simulate_turn(self) -> dict[str, Any]:
        if not self.factory or not self.strategy:
            print("\nGame engine not initiated!")
            return {'error': 'Game engine not initiated'}
        hand_size = randrange(3, 8)
        hand: list[Card] = self.factory.create_themed_deck(hand_size)['cards']
        actions = self.strategy.execute_turn(hand, ['Enemy Player'])
        self.stats['cards_created'] += hand_size
        self.stats['total_damage'] += actions['damage_dealt']
        self.stats['turns_simulated'] += 1
        return {
            'hand': [card.name for card in hand],
            'strategy': self.strategy.get_strategy_name(),
            'actions': actions
        }

    def get_engine_status(self) -> dict[str, Any]:
        return self.stats
