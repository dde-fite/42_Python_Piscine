from typing import Any
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy
                         ) -> None:
        self.factory = factory
        self.strategy = strategy
        print(f"Factory: {type(factory).__name__}\n"
              f"Strategy {type(strategy).__name__}\n"
              f"Available types:")

    def simulate_turn(self) -> dict[str, Any]:
        if not self.factory or not self.strategy:
            print("\nGame engine not initiated!")
            return {'error': 'Game engine not initiated'}

    def get_engine_status(self) -> dict[str, Any]:
        if not self.factory or not self.strategy:
            print("\nGame engine not initiated!")
            return {'error': 'Game engine not initiated'}
