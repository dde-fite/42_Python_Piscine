from typing import Any
from random import choice
from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.available: dict[str, dict[str, list[Any]]] = {
            'creature': {
                'dragon': ["Fire Dragon", 7, "Legendary", 8, 8],
                'goblin': ["Goblin Warrior", 2, "Common", 2, 2]
            },
            'spell': {
                'fireball': ["Fireball", 4, "Rare", "damage"]
            },
            'artifact': {
                'mana_ring': ["Mana Ring", 1, "Common", 5, "mana_boost"]
            }
        }

    def create_creature(self, name_or_power: str | int | None = None
                        ) -> Card:
        try:
            card = []
            if isinstance(name_or_power, str):
                card = self.available['creature'][name_or_power]
            elif isinstance(name_or_power, int):
                card = list(self.available['creature'].values())[name_or_power]
            return CreatureCard(*card)
        except (KeyError, IndexError):
            return CreatureCard("Default", 0, "None", 0, 0)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        try:
            card = []
            if isinstance(name_or_power, str):
                card = self.available['spell'][name_or_power]
            elif isinstance(name_or_power, int):
                card = list(self.available['spell'].values())[name_or_power]
            return SpellCard(*card)
        except (KeyError, IndexError):
            return SpellCard("Default", 0, "None", "None")

    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> Card:
        try:
            card = []
            if isinstance(name_or_power, str):
                card = self.available['artifact'][name_or_power]
            elif isinstance(name_or_power, int):
                card = list(self.available['artifact'].values())[name_or_power]
            return ArtifactCard(*card)
        except (KeyError, IndexError):
            return ArtifactCard("Default", 0, "None", 0, "None")

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck: dict[str, Any] = {
            'cards': [],
            'size': size
        }
        cards = deck['cards']
        for _ in range(size):
            function = None
            cat = None
            while not function:
                cat = choice(list(self.available.keys()))
                function = getattr(self, f"create_{cat}", None)
            key = choice(list(self.available[cat].keys()))
            cards.append(function(key))
        return deck

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            key: list(value.keys()) for key, value in self.available.items()
        }
