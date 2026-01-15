def water_plants(plant_list: list[str]) -> None:
    """Waters the plants in a list.

    Args:
        plant_list (list[str]): Lists of the plants names
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Runs water_plants() with correct test values and with incorrect ones."""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


test_watering_system()
