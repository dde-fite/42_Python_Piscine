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
                'goblin': ["Goblin Warrior", 2, "Common", 2, 2],
                'default': ["Default", 0, "None", 0, 0]
            },
            'spell': {
                'fireball': ["Fireball", 4, "Rare", "damage"],
                'default': ["Default", 0, "None", "None"]
                },
            'artifact': {
                'mana_ring': ["Mana Ring", 1, "Common", 5, "mana_boost"],
                'default': ["Default", 0, "None", 0, "None"]
                }
        }

    def create_creature(self, name_or_power: str | int | None = None
                        ) -> Card:
        if isinstance(name_or_power, str):
            card = self.available['creature'].get(
                name_or_power, self.available['creature']['default']
                )
        elif isinstance(name_or_power, int):
            card = list(self.available['creature'].values())[name_or_power]
        else:
            card = self.available['creature']['default']
        return CreatureCard(*card)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            card = self.available['spell'].get(
                name_or_power, self.available['spell']['default']
                )
        elif isinstance(name_or_power, int):
            card = list(self.available['spell'].values())[name_or_power]
        else:
            card = self.available['spell']['default']
        return SpellCard(*card)

    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> Card:
        if isinstance(name_or_power, str):
            card = self.available['artifact'].get(
                name_or_power, self.available['artifact']['default']
                )
        elif isinstance(name_or_power, int):
            card = list(self.available['artifact'].values())[name_or_power]
        else:
            card = self.available['artifact']['default']
        return ArtifactCard(*card)

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck: dict[str, Any] = {
            'cards': [],
            'size': size
        }
        cards = deck['cards']
        for _i in range(0, size):
            function = None
            cat = None
            while not function:
                cat = choice(list(self.available.keys()))
                function = getattr(self, f"create_{cat}", None)
            cards.append(function(choice(list(self.available[cat].values()))))
        return deck

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            key: list(value.keys()) for key, value in self.available.items()
        }
