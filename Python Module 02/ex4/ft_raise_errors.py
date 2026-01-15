def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Evaluates the state of the plant's water level and sunlight hours.

    If the name of the plant is empty or it has bad conditions levels,
    it raises an error.

    Args:
        plant_name (str): Name of the plant
        water_level (int): Water level of the plant.
        sunlight_hours (int): Sunlight hours of the plant

    Raises:
        ValueError: If the name of the plant is empty or it has bad conditions.
    """
    try:
        if plant_name is None or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 0)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low "
                             "(min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high "
                             "(max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e.args[0]}")


def test_plant_checks() -> None:
    """Runs check_plant_health() with a different sets of values."""
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("tomato", 10, 5)

    print("\nTesting empty plant name...")
    check_plant_health("", 4, 10)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 1)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 3, 0)

    print("\nAll error raising tests completed!")


test_plant_checks()
