from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):

    @abstractmethod
    def attack(self, target: Card) -> dict[str, Any]: ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]: ...

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]: ...
