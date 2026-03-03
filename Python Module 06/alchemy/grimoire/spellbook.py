def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    val_result = validate_ingredients(ingredients)
    if val_result.split("-")[-1].strip() == "VALID":
        return f"Spell recorded: {spell_name} ({val_result})"
    else:
        return f"Spell rejected: {spell_name} ({val_result})"
