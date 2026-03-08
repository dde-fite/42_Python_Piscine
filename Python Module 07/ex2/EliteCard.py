from typing import Any
from random import randrange
from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)
        self.game_state: dict[str, Any] | None = None
        self.combats: dict[str, list[dict[str, Any]]] = {
            'attack': [],
            'defense': []
        }
        self.magic: dict[str, list[dict[str, Any]]] = {
            'spell': [],
            'channel': []
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if not self.is_playable(game_state["mana"]):
            return {}
        self.game_state = game_state
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

    def cast_spell(self, spell_name: str, targets: list[Card]
                   ) -> dict[str, Any]:
        spell_name = spell_name.strip().lower()
        health_change: int = 0
        if spell_name == "fireball":
            health_change = -(randrange(0, 10))
        elif spell_name == "heal":
            health_change = randrange(0, 10)
        else:
            return {"error": "Spell not recognized"}
        for target in targets:
            target.health += health_change
        data: dict[str, Any] = {
            'caster': self.name,
            'spell': spell_name.title(),
            'targets': [target.name for target in targets],
            'mana_used': self.cost
        }
        self.magic['spell'].append(data)
        return data

    def channel_mana(self, amount: int) -> dict[str, Any]:
        total_mana: int
        if self.game_state:
            self.game_state['mana'] += amount
            total_mana = self.game_state['mana']
        else:
            total_mana = randrange(0, 10) + amount
        data: dict[str, Any] = {
            'channeled': amount,
            'total_mana': total_mana
        }
        self.magic['channel'].append(data)
        return data

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            'total_interactions': len(self.magic),
            'spells': len(self.magic['spell']),
            'channels': len(self.magic['channel']),
            'registry': self.magic
            }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            'total_interactions': len(self.combats),
            'attacks': len(self.combats['attack']),
            'defenses': len(self.combats['defense']),
            'registry': self.combats
        }
