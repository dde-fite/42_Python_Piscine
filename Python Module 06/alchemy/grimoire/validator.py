def validate_ingredients(ingredients: str) -> str:
    """
    Validates that ingredients match the available ones (fire, water, earth, \
        air).

    Args:
        ingredients (str): Ingredients separated with ' '(space).

    Returns:
        str: Ingredients + VALID. In case of invalid: Ingredients + INVALID.
    """
    for i in ingredients.split(" "):
        if i not in ("fire", "water", "earth", "air"):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
