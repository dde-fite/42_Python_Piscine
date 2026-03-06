from typing import Any
from .Deck import Deck
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard

game_state: dict[str, Any] = {
    "mana": 10,
}

print("\n=== DataDeck Deck Builder ===\n"
      "\nBuilding deck with different card types...")
deck = Deck()
deck.add_card(
    SpellCard("Lightning Bolt", 3, "Normal", "Deal 3 damage to target")
)
deck.add_card(
    ArtifactCard("Mana Crystal", 2, "Rare", 4, "Permanent: +1 mana per turn")
)
deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
print(f"Deck stats: {deck.get_deck_stats()}")

print("\nDrawing and playing cards:")
while (card := deck.draw_card()):
    print(f"\nDrew: {card.name}\n"
          f"Play result: {card.play(game_state)}")

print("\nPolymorphism in action: Same interface, different card behaviors!")
