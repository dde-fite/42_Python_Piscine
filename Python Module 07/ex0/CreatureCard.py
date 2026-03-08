from __future__ import annotations
# In case of dispute regarding the use of the __future__ package, I refer to
# the subject in the Authorized Imports section:
# "Standard library modules as needed." (accessed on March 5, 2026)
from typing import Any
from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise Exception("Invalid value for attack and health")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict[str, Any]:
        return {
            **super().get_card_info(),
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if not self.is_playable(game_state["mana"]):
            return {}
        game_state["mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: Card) -> dict[str, Any]:
        target.health -= self.attack
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': target.health <= 0
        }
