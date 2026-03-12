from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from .EliteCard import EliteCard

game_state = {
    'mana': 9
}

card = [m for m in dir(Card) if callable(getattr(Card, m))
        and not m.startswith('__')]
combatable = [m for m in dir(Combatable) if callable(getattr(Combatable, m))
              and not m.startswith('__')]
magical = [m for m in dir(Magical) if callable(getattr(Magical, m))
           and not m.startswith('__')]

elite_card = EliteCard("Arcane Warrior", 5, "Legendary")

spell = elite_card.cast_spell(
        'Fireball',
        [
            EliteCard('Enemy1', 4, 'Legendary'),
            EliteCard('Enemy2', 4, 'Legendary')
        ]
        )


print(
    "\n=== DataDeck Ability System ===\n"

    "\nEliteCard capabilities:\n"
    f"- Card: {card}\n"
    f"- Combatable: {combatable}\n"
    f"- Magical: {magical}\n"

    f"\nPlaying {elite_card.name} ({type(elite_card).__name__}): \
    {'' if elite_card.play(game_state) else ' Failed'}\n"

    "\nCombat phase:\n"
    f"Attack result: {elite_card.attack(EliteCard('Enemy', 4, 'Legendary'))}\n"
    f"Defense result: {elite_card.defend(5)}\n"

    "\nMagic phase:\n"
    f"Spell cast: {spell}\n"
    f"Mana channel: {elite_card.channel_mana(3)}\n"

    "\nMultiple interface implementation successful!\n"

    "\nEXTRA (I know the example in the statement doesn't ask for it,\n"
    "but as it says, it's just an example)\n"

    f"\n=== {elite_card.name} Analytics ===\n"
    f"\nCombat Stats: {elite_card.get_combat_stats()}\n"
    f"\nMagic Stats: {elite_card.get_magic_stats()}"
)
