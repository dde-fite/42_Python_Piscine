def get_items_value(player) -> int:  # type: ignore
    """Returns the value of all the items in the player's inventory.

    Args:
        player (_type_): Dictionary for player's info.

    Returns:
        int: Value of inventory items
    """
    value = 0
    for item_inv in player["inventory"].values():
        value += item_inv["quantity"] * item_inv["price"]
    return value


def get_items_quantity(player) -> int:  # type: ignore
    """Returns the quantity of items in the player's inventory.

    Args:
        player (_type_): Dictionary for player's info.

    Returns:
        int: Quantity of inventory items
    """
    quantity = 0
    for item_inv in player["inventory"].values():
        quantity += item_inv["quantity"]
    return quantity


def show_inventory(player: dict) -> None:  # type: ignore
    """Prints information about the player's inventory and its items.

    Lists each item type formatted as: <item> (category,..) <quantity>x @ \
    <value> gold each = <quantity * value> gold

    Then, it gets statistics like total value, item count, and categories.

    Args:
        player (dict): Dictionary for player's info.
    """
    total_categories: dict[str, int] = {}

    print(f"\n=== {player["name"]}'s Inventory ===")

    for item, item_inv in player["inventory"].items():
        value = item_inv['quantity'] * item_inv['price']

        category = item_inv['category'][0]
        total_categories[category] = (
            total_categories.get(category, 0) + item_inv["quantity"]
        )

        print(f"{item} ({', '.join(item_inv['category'])}): "
              f"{item_inv['quantity']}x @ {item_inv['price']} "
              f"gold each = {value} gold")

    category_text = ", ".join(
        f"{cat}({qty})" for cat, qty in total_categories.items()
    )

    print(f"\nInventory value: {get_items_value(player)} gold\n"
          f"Item count: {get_items_quantity(player)} items\n"
          f"Categories: {category_text}",)


def notify_update(s: str = "") -> None:
    """Notifier for changes in inventories

    Args:
        s (str): Message about the changes.
    """
    print(f"\n=== Updated Inventories ===\n{s}")


def transaction(player_from: dict, player_to: dict, item: str,  # type: ignore
                quantity: int) -> None:
    """Makes a transition of items between players and notifies the changes.

    Args:
        player_from (dict): Dictionary for sender player's info.
        player_to (dict): Dictionary for receiver player's info.
        item (str): Name of item to send.
    """
    print(f"\n=== Transaction: {player_from['name']} gives {player_to['name']}"
          f" {quantity} potion ===")

    if item not in player_from['inventory']:
        print(f"{player_from['name']} has no {item}")
        return
    item_f = player_from['inventory'][item]
    if item_f['quantity'] < quantity:
        print(f"{player_from['name']} only has x{item_f['quantity']} {item}")
        return

    item_f['quantity'] -= quantity
    if item in player_to['inventory']:
        player_to['inventory'][item]['quantity'] += quantity
    else:
        player_to['inventory'][item] = {
            "category": item_f['category'],
            "quantity": quantity,
            "price": item_f['price'],
        }

    print("Transaction successful!")
    notify_update(
        f"{player_from['name']} {item}: {item_f['quantity']}\n"
        f"{player_to['name']} {item}: "
        f"{player_to['inventory'][item]['quantity']}"
    )


def get_rare_items(players: dict) -> list:  # type: ignore
    """Returns unique items only present in 1 player at the same time.

    Args:
        players (dict): Dictionary for player's info.

    Returns:
        list: List of rare items
    """
    item_count: dict[str, int] = {}

    for player in players.values():
        for item in player["inventory"].keys():
            item_count[item] = item_count.get(item, 0) + 1

    rare = [item for item, count in item_count.items() if count == 1]

    return rare


def print_analytics(players: dict):  # type: ignore
    """Collects data of the players and it's inventories

    Args:
        players (dict): Dictionary for player's info.
    """
    valuable, most = {}, {}

    for player in players:
        valuable, most = players[player], players[player]
        break

    for player in players.values():

        if get_items_value(player) > get_items_value(valuable):
            valuable = player
        if get_items_quantity(player) > get_items_quantity(most):
            most = player

    print("\n=== Inventory Analytics ===\n"
          f"Most valuable player: {valuable['name']} ("
          f"{get_items_value(valuable)} gold)\n"
          f"Most items: {most['name']} ({get_items_quantity(most)} items)\n"
          f"Rarest items: {', '.join(get_rare_items(players))}")


players = {
    "alice": {
        "name": "Alice",
        "inventory": {
            "sword": {
                "category": ["weapon", "rare"],
                "quantity": 1,
                "price": 500,
            },
            "potion": {
                "category": ["consumable", "common"],
                "quantity": 5,
                "price": 50,
            },
            "shield": {
                "category": ["armor", "uncommon"],
                "quantity": 1,
                "price": 200,
            }
        }
    },
    "bob": {
        "name": "Bob",
        "inventory": {
            "magic_ring": {
                "category": ["weapon", "rare"],
                "quantity": 1,
                "price": 500,
            },
            "shield": {
                "category": ["armor", "uncommon"],
                "quantity": 1,
                "price": 200,
            }
        }
    }
}

print("=== Player Inventory System ===")
show_inventory(players['alice'])
transaction(players['alice'], players['bob'], 'potion', 2)
print_analytics(players)
