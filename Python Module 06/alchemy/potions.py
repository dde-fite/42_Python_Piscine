from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Heals a potion with fire and water"""
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Heals a potion with earth and fire"""
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Heals a potion with air and water"""
    return (f"Invisibility potion brewed with {create_air()} and "
            f"{create_water()}")


def wisdom_potion() -> str:
    """Heals a potion with all the available elements"""
    return (f"Wisdom potion brewed with all elements: {create_fire()} and "
            f"{create_water()} and {create_earth()} and {create_air()}")
