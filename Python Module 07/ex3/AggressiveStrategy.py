from typing import Any
from random import sample, randrange
from ex0.Card import Card


class AggressiveStrategy:
    def execute_turn(self, hand: list[Card], battlefield: list[Card]
                     ) -> dict[str, Any]:
        cards_played: list[Card] = sample(
            hand, (randrange(1, len(hand) + 1) if len(hand) > 1 else 1)
            )
        print(cards_played)
        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': sum([card.cost for card in cards_played]),
            'targets_attacked': sample(
                battlefield,
                (randrange(1, len(battlefield) + 1)
                 if len(battlefield) > 1 else 1)
            ),
            'damage_dealt': randrange(0, 30)
        }

    def get_strategy_name(self) -> str:
        return type(self).__name__

    def prioritize_targets(self, available_targets: list) -> list:
        pass
