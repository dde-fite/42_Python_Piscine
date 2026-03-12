from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard

tournament = TournamentPlatform()

print(
    "\n=== DataDeck Tournament Platform ===\n"

    "\nRegistering Tournament Cards...\n"

    f"\n{tournament.register_card(TournamentCard("Fire Dragon", 5, "Normal", "dragon_001"))}\n"
)



tournament.register_card(
    TournamentCard("Ice Wizard", 8, "Rare", "wizard_001")
)


