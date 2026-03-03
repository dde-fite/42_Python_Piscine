def validate_ingredients(ingredients: str) -> str:
    for i in ingredients.split(" "):
        if i not in ("fire", "water", "earth", "air"):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
