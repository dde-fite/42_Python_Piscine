from typing import Any
from .Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        pass

    def attack(self, target: Card) -> dict[str, Any]:
        pass

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        pass

    def get_combat_stats(self) -> dict[str, Any]:
        pass

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict[str, Any]:
        pass

    def get_tournament_stats(self) -> dict[str, Any]:
        pass
