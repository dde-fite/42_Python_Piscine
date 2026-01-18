def print_player_achievements(players: dict[str, set[str]], player: str
                              ) -> None:
    print(f"Player {player} achievements: {players[player]}")


def print_stats(players: dict[str, set[str]]) -> None:

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


def compare_players(players: dict[str, set[str]], player_a: set[str],
                    player_b: set[str]) -> None:
    print()


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
