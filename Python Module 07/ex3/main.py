from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


print("\n=== DataDeck Game Engine ==="
      "\nConfiguring Fantasy Card Game...")

engine = GameEngine()

engine.configure_engine(
    FantasyCardFactory(),
    AggressiveStrategy()
)

turn = engine.simulate_turn()

print(f"Available types: {engine.factory.get_supported_types()}\n"

      "\nSimulating aggressive turn...\n"
      f"Hand: {turn['hand']}\n"

      "\nTurn execution:\n"
      f"Strategy: {turn['strategy']}\n"
      f"Actions: {turn['actions']}\n"

      "\nGame Report:\n",
      f"{engine.get_engine_status()}\n"

      "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
      )
