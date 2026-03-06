from typing import Any
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.__type: str = effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if not self.is_playable(game_state["mana"]):
            return {}
        game_state["mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.__type
        }

    def resolve_effect(self, targets: list[Card]) -> dict[str, Any]:
        return {
            **super().get_card_info(),
            'type': self.__type
        }
