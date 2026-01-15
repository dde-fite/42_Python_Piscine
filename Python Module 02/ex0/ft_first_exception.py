def check_temperature(temp_str: str) -> int | None:
    """Parses the temperature as an int and validates the value.

    First converts the temperature to an integer using int() and check if it
    is not a valid value.

    Then checks that the temperature is between 0ºC and 40ºC.

    Args:
        temp_str (str): Temperature to check

    Returns:
        int | None: If there are no errors, returns the temperature parsed.
    """
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
    """Calls check_temperature() for each value in a to_test list."""
    to_test: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for test in to_test:
        print()
        check_temperature(test)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
