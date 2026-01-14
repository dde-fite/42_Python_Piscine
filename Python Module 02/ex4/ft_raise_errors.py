def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
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
