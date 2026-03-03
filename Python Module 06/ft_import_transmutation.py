import alchemy.elements
from alchemy.elements import create_earth, create_fire, create_water
from alchemy.potions import strength_potion, healing_potion as heal

print("\n=== Import Transmutation Mastery ===\n"

      "\nMethod 1 - Full module import:\n"
      f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"

      "\nMethod 2 - Specific function import:\n"
      f"create_water(): {create_water()}\n"

      "\nMethod 3 - Aliased import:\n"
      f"heal(): {heal()}\n"

      "\nMethod 4 - Multiple imports:\n"
      f"create_earth(): {create_earth()}\n"
      f"create_fire(): {create_fire()}\n"
      f"strength_potion(): {strength_potion()}\n"

      "\nAll import transmutation methods mastered!")
