from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if not self.is_playable(game_state["mana"]):
            return {}
        game_state["mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict[str, Any]:
        return {
            **super().get_card_info(),
            'effect': self.effect
        }
