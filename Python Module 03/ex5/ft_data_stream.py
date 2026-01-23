import time


def game_event_stream(n: int):  # type: ignore
    """Streams game events from a list and generates them.

    Args:
        n (int): Number of events to generate.

    Yields:
        list[dict]: Dictionary of event details.
    """
    players = [{"name": "alice", "level": 5}, {"name": "bob", "level": 8},
               {"name": "charlie", "level": 12}, {"name": "dan", "level": 15},
               {"name": "eve", "level": 1}, {"name": "frank", "level": 4}]
    actions = ["killed monster", "found treasure", "leveled up",
               "ate a hamburger", "crocheted a blanket",
               "discovered a location", "completed a cave", "tamed the dragon",
               "finished his studies"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        yield {"id": i, "player": player["name"], "level": player["level"],
               "action": action}


def process_game_stream(n: int):  # type: ignore
    """Calls game_event_stream() and calculates statistics based on its output.

    Args:
        n (int): Number of events to generate.
    """
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    start_time = time.time()

    print(f"\nProcessing {n} game events...\n")
    for event in game_event_stream(n):
        total_events += 1
        if event["level"] >= 10:
            high_level_count += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        if event["action"] == "leveled up":
            levelup_count += 1
        print(f"Event {event['id']}: Player {event['player']} "
              f"(level {event['level']}) {event['action']}")

    print("\n=== Stream Analytics ===\n"
          f"Total events processed: {total_events}\n"
          f"High-level players (10+): {high_level_count}\n"
          f"Treasure events: {treasure_count}\n"
          f"Level-up events: {levelup_count}\n"
          f"\nMemory usage: Constant (streaming)\n"
          f"Processing time: {time.time() - start_time:.3}")


def fibo_sequence(n: int):  # type: ignore
    """Generates a fibonacci sequence.

    Args:
        n (int): Numbers to generate.

    Yields:
        int: Current fibonacci number.
    """
    prev: int = 0
    prev2: int = 0
    for i in range(n):
        if i == 1:
            prev2 = 1
        actual = prev + prev2
        prev2 = prev
        prev = actual
        yield actual


def prime_nums(n: int):  # type: ignore
    """_summary_

    Args:
        n (int): Numbers to generate.

    Yields:
        int: Current prime number.
    """
    def __is_prime(n: int) -> int:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    actual: int = 1
    for _i in range(n):
        actual += 1
        while not __is_prime(actual):
            actual += 1
        yield actual


print("=== Game Data Stream Processor ===")
process_game_stream(1000)
print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): ", end='')
for n in fibo_sequence(10):
    print(f"{n}, ", end='')
print("\nPrime numbers (first 5): ", end='')
for n in prime_nums(5):
    print(f"{n}, ", end='')
print()
