def check_temperature(temp_str: str) -> int | None:
    print(f"Testing temperature: {temp_str}")
    try:
        parsed: int = int(temp_str)
        if parsed < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
            return None
        elif parsed > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return None
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return parsed
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    to_test: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for test in to_test:
        print()
        check_temperature(test)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
