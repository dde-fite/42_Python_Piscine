from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard

tournament = TournamentPlatform()

fire_dragon = TournamentCard("Fire Dragon", 5, "Normal", "dragon_001")
ice_wizard = TournamentCard("Ice Wizard", 8, "Rare", "wizard_001", 1150)

print(
    "\n=== DataDeck Tournament Platform ===\n"

    "\nRegistering Tournament Cards...\n"

    f"\n{tournament.register_card(fire_dragon)}\n"
    f"\n{tournament.register_card(ice_wizard)}\n"

    "\nCreating tournament match...\n"
    f"{tournament.create_match('dragon_001', 'wizard_001')}"

    "\nTournament Leaderboard:"
    f""
)
