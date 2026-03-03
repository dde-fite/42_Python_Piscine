def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Records the spell passed and validates the ingredients.

    Args:
        spell_name (str): Spell's name.
        ingredients (str): Ingredients separated with ' '(space).

    Returns:
        str: Result of spell and validation results.
    """
    from .validator import validate_ingredients
    val_result = validate_ingredients(ingredients)
    if val_result.split("-")[-1].strip() == "VALID":
        return f"Spell recorded: {spell_name} ({val_result})"
    else:
        return f"Spell rejected: {spell_name} ({val_result})"
