def show_inventory(player_data: dict[dict[str, str, str]]) -> None:
    print("=== Player Inventory System ===\n"
          f"\n=== {}'s Inventory ===")
    for item in player_data:
        categories: str = ""
        for cat in player_data[item]['category']:
            if categories == "":
                categories = cat
            else:
                categories += f", {cat}"
        print(f"{item} ({categories}): {player_data[item]['quantity']}x @ s"
              f"{player_data[item]['price']} gold each = "
              f"{player_data[item]['price'] * player_data[item]['quantity']}")


alice = {
    "sword": {
        "category": ["weapon", "rare"],
        "quantity": 1,
        "price": 500
    },
    "potion": {
        "category": ["consumable", "common"],
        "quantity": 5,
        "price": 50
    },
    "shield": {
        "category": ["armor", "uncommon"],
        "quantity": 1,
        "price": 200
    }
}

