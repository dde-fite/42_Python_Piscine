def print_player_achievements(players: dict[str, set[str]], player: str
                              ) -> None:
    """Prints all the achivements of a player in a dictionary.

    Args:
        players (dict[str, set[str]]): Achievements of each player.
        player (str): Name of the player.
    """
    print(f"Player {player} achievements: {players[player]}")


def print_stats(players: dict[str, set[str]]) -> None:
    """Prints all the stats of the achievements.

    Args:
        players (dict[str, set[str]]): Achievements of each player.
    """
    all_sets = list(players.values())
    unique: set[str] = set().union(*all_sets)
    common: set[str] = set.intersection(*all_sets)
    rare: set[str] = set()

    for ach in unique:
        count: int = 0
        for ply in players:
            if ach in players[ply]:
                count += 1
        if count == 1:
            rare.add(ach)

    print("\n=== Achievement Analytics ==="
          f"\nAll unique achievements: {unique}\n"
          f"Total unique achievements: {len(unique)}\n"
          f"\nCommon to all players: {common}\n"
          f"Rare achievements (1 player): {rare}")


def compare_players(players: dict[str, set[str]], player_a: str,
                    player_b: str) -> None:
    """Compares the achievements of two players given.

    Args:
        players (dict[str, set[str]]): Achievements of each player.
        player_a (str): Name of player A.
        player_b (str): Name of player B.
    """
    common: set[str] = players[player_a].intersection(players[player_b])
    a_unique: set[str] = players[player_a].difference(players[player_b])
    b_unique: set[str] = players[player_b].difference(players[player_a])
    print(f"\n{player_a.capitalize()} vs {player_b.capitalize()} "
          f"common: {common}")
    print(f"{player_a.capitalize()} unique: {a_unique}")
    print(f"{player_b.capitalize()} unique: {b_unique}")


players = {
    "alice": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
    "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
    "charlie": {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                'perfectionist'}
}

print("=== Achievement Tracker System ===\n")
print_player_achievements(players, "alice")
print_player_achievements(players, "bob")
print_player_achievements(players, "charlie")
print_stats(players)
compare_players(players, "alice", "bob")
