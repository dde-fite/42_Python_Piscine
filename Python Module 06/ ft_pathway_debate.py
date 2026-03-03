import alchemy
from alchemy.transmutation import (lead_to_gold, stone_to_gem,
                                   philosophers_stone, elixir_of_life)

print("\n=== Pathway Debate Mastery ===\n"

      "\nTesting Absolute Imports (from basic.py):\n"
      f"lead_to_gold(): {lead_to_gold()}\n"
      f"stone_to_gem(): {stone_to_gem()}\n"

      "\nTesting Relative Imports (from advanced.py):\n"
      f"philosophers_stone(): {philosophers_stone()}\n"
      f"elixir_of_life(): {elixir_of_life()}\n"

      "\nTesting Package Access:\n"
      "alchemy.transmutation.lead_to_gold(): "
      f"{alchemy.transmutation.lead_to_gold()}\n"
      "alchemy.transmutation.philosophers_stone(): "
      f"{alchemy.transmutation.philosophers_stone()}\n"

      "\nBoth pathways work! Absolute: clear, Relative: concise")
