import alchemy

print("\n=== Sacred Scroll Mastery ===\n"
      "\nTesting direct module access:\n"
      f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
      f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\n"
      f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\n"
      f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n"

      f"\nTesting package-level access (controlled by __init__.py):\n"
      f"alchemy.create_fire(): {alchemy.create_fire()}\n"
      f"alchemy.create_water(): {alchemy.create_water()}")

try:
    alchemy.create_earth()
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    alchemy.create_air()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:\n"
      f"Version: {alchemy.__version__}\n"
      f"Author: {alchemy.__author__}")
