ACH_BY_RARITY = {
    "low": [
        "first_kill",
        "level_10",
        "collector",
        "explorer",
        "daily_player"
    ],
    "medium": [
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "strategist",
    ],
    "high": [
        "perfectionist",
        "legend",
    ]
}

players = [
    {
        "name": "alice",
        "score": 2050,
        "active": True,
        "achievements": [
            "first_kill", "level_10", "treasure_hunter",
            "speed_demon", "explorer", "strategist"
        ],
        "region": "east"
    },
    {
        "name": "bob",
        "score": 1750,
        "active": True,
        "achievements": [
            "first_kill", "level_10", "boss_slayer",
            "collector", "daily_player"
        ],
        "region": "north"
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "achievements": [
            "flevel_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist", "legend"
        ],
        "region": "central"
    },
    {
        "name": "diana",
        "score": 1075,
        "active": False,
        "achievements": [
            "first_kill", "level_10", "boss_slayer",
            "collector", "explorer"
        ],
        "region": "central"
    },
]

unique_ply: set[object] = {p['name'] for p in players}
unique_ach: set[object] = \
    {ach for player in players for ach in player['achievements']}
top_ply_score, top_ply_ach, top_ply_name = \
    max([(p["score"], len(p["achievements"]), p["name"]) for p in players])

print("=== Game Analytics Dashboard ===\n"
      "\n=== List Comprehension Examples ===\n"
      "High scorers (>2000): "
      f"{[i['name'] for i in players if i['score'] > 2000]}\n"
      f"Scores doubled: {[i['score'] * 2 for i in players]}\n"
      f"Active players: {[i['name'] for i in players if i['active']]}\n"

      "\n=== Dict Comprehension Examples ===\n"
      f"Player scores: {({i['name']: i['score'] for i in players})}\n"
      "Score categories: "
      f"{({cat: len(values) for cat, values in ACH_BY_RARITY.items()})}\n"
      "Achievement counts: "
      f"{({i['name']: len(i['achievements']) for i in players})}\n"

      "\n=== Set Comprehension Examples ===\n"
      f"Unique players: {unique_ply}\n"
      f"Unique achievements: {unique_ach}\n"
      f"Active regions: {({player['region'] for player in players})}\n"

      "\n=== Combined Analysis ===\n"
      f"Total players: {len(players)}\n"
      f"Total unique achievements: {len(unique_ach)}\n"
      "Average score: "
      f"{sum([i['score'] for i in players]) / len(unique_ply)}\n"
      f"Top performer: {top_ply_name} ({top_ply_score} points, {top_ply_ach} "
      "achievements)\n"
      )
