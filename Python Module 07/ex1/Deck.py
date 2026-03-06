from typing import Any
from random import shuffle
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if card in self.cards:
            return
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card | None:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        return {
            'total_cards': len(self.cards),
            'creatures': len(
                [card for card in self.cards if isinstance(card, CreatureCard)]
            ),
            'spells': len(
                [card for card in self.cards if isinstance(card, SpellCard)]
            ),
            'artifacts': len(
                [card for card in self.cards if isinstance(card, ArtifactCard)]
            ),
            'avg_cost': '%.1f' % (sum(
                            [card.cost for card in self.cards]
                        ) / len(self.cards))
        }
