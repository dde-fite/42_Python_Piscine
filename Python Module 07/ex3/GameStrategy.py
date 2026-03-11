from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: list[Card], battlefield: list[str]
                     ) -> dict[str, Any]: ...

    @abstractmethod
    def get_strategy_name(self) -> str: ...

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Card]
                           ) -> list[Card]: ...
