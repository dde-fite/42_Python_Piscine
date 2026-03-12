# REMEMBER TO TEST EXERCISES WITH python -m ex0.main FROM REPO'S ROOT

from typing import Any
from .CreatureCard import CreatureCard

game_state: dict[str, Any] = {
    "mana": 8,
}

creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
creature_2 = CreatureCard("Goblin Warrior", 6, "Rare", 3, 7)

print("\n=== DataDeck Card Foundation ===\n"
      "\nTesting Abstract Base Class Design:"

      "\nCreatureCard Info: \n"
      f"{creature.get_card_info()}"

      "\nPlaying Fire Dragon with 6 mana available:\n"
      f"Playable: {creature.is_playable(game_state['mana'])}\n"
      f"Play result: {creature.play(game_state)}\n"

      "\nFire Dragon attacks Goblin Warrior:\n"
      f"Attack result: {creature.attack_target(creature_2)}\n"

      "\nTesting insufficient mana (3 available):\n"
      f"Playable: {creature.is_playable(game_state['mana'])}\n"
      f"{creature.play(game_state)}\n"

      "\nAbstract pattern successfully demonstrated!")
