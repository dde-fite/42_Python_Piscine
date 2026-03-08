from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[Card]
                   ) -> dict[str, Any]: ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]: ...

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]: ...
