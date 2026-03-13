from typing import Any
from random import randrange
from .Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str,
                 base_rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.id: str = id
        self.base_rating = base_rating
        self.stats = {
            'wins': 0,
            'losses': 0
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

    def attack(self, target: Card) -> dict[str, Any]:
        damage = randrange(0, 5)
        combat_type = "melee"
        target.health -= damage
        data: dict[str, Any] = {
            'attacker': self.name,
            'target': target.name,
            'damage': damage,
            'combat_type': combat_type
        }
        self.combats['attack'].append(data)
        return data

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        damage_blocked = randrange(0, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        data: dict[str, Any] = {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > 0
        }
        self.combats['defense'].append(data)
        return data

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            'total_interactions': len(self.combats),
            'attacks': len(self.combats['attack']),
            'defenses': len(self.combats['defense']),
            'registry': self.combats
        }

    def calculate_rating(self) -> int:
        return (self.base_rating +
                (self.stats['wins'] - self.stats['losses']) * 16)

    def update_wins(self, wins: int) -> None:
        self.stats['wins'] += wins

    def update_losses(self, losses: int) -> None:
        self.stats['losses'] += losses

    def get_rank_info(self) -> dict[str, Any]:
        pass

    def get_tournament_stats(self) -> dict[str, Any]:
        return self.stats.copy()
