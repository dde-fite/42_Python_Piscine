import sys

USAGE_MESSAGE = "Usage: python3 ft_score_analytics.py <score1> <score2> ..."

try:
    if len(sys.argv) < 2:
        raise ValueError
except ValueError:
    print(f"No scores provided. {USAGE_MESSAGE}")
    exit(1)

scores: list[int] = []

for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f"Invalid integer value: {arg}. {USAGE_MESSAGE}")
        exit(1)

print("=== Player Score Analytics ===\n"
      f"Scores processed: {scores}\n"
      f"Total players: {len(scores)}\n"
      f"Total score: {sum(scores)}\n"
      f"Average score: {sum(scores) / len(scores)}\n"
      f"High score: {max(scores)}\n"
      f"Low score: {min(scores)}\n"
      f"Score range: {max(scores) - min(scores)}")
