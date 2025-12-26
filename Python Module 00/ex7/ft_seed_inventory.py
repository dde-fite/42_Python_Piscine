def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Prints information about a seed from the inventory.

    Args:
        seed_type (str): Name of the seed type
        quantity (int): Quantity number
        unit (str): Type of the unit. Accepted units are: packets, grams, area
    """
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} "
              "square meters")
    else:
        print("Unknown unit type")
