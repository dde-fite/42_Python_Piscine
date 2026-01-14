class GardenError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class PlantError(GardenError):
    def __init__(self, msg: str, plant_name: str = ""):
        self.msg = msg
        self.plant_name = plant_name


class WaterError(GardenError):
    def __init__(self, msg: str):
        self.msg = msg


class Plant:
    """A class representing a Plant.

    Attributes:
        name (str): Plant name
    """

    def __init__(self, name: str, water: int, sun: int) -> None:
        """Initialize a Plant object.

        Args:
            name (str): Plant name
        """
        self.__name: str = name
        self.__water: int = water
        self.__sun: int = sun

    def get_name(self) -> str:
        """Returns the name of the Plant."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Sets the name of the Plant."""
        try:
            if name is None or name == "":
                raise PlantError("Plant name cannot be empty!")
            self.__name = name
        except PlantError as e:
            print(f"Error setting plant name: {e.msg}")

    def get_water(self) -> int:
        """Returns the water of the Plant."""
        return self.__water

    def get_sun(self) -> int:
        """Returns the sun of the Plant."""
        return self.__sun


class GardenManager():
    """A manager class responsible for handling the garden.

    Attributes:
        plants (Garden): List of plants in the garden.
    """
    def __init__(self) -> None:
        """Initialize a Garden object."""
        self.__plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden.

        Args:
            plant: Plant instance to add
        """
        try:
            if plant.get_name() is None or plant.get_name() == "":
                raise PlantError("Plant name cannot be empty!")
            self.__plants.append(plant)
            print(f"Added {plant.get_name()} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e.msg}")

    def remove_plant(self, plant: Plant) -> None:
        """Removes a plant from the garden.

        Args:
            plant: Plant instance to remove
        """
        self.__plants.remove(plant)
        print(f"Removed {plant.get_name()}")

    def get_plants(self) -> list[Plant]:
        """Returns a copy of the plants in the garden."""
        return self.__plants.copy()

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.__plants:
                print(f"Watering {plant.get_name()} - success")
        except WaterError as e:
            print(f"Error watering: {e.msg}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        try:
            for plant in self.__plants:
                water = plant.get_water()
                sun = plant.get_sun()
                if water < 1:
                    raise PlantError(f"Water level {water} is too low (min 0)",
                                     plant.get_name())
                if water > 10:
                    raise PlantError(f"Water level {water} is too high "
                                     "(max 10)", plant.get_name())
                if sun < 2:
                    raise PlantError(f"Sunlight hours {sun} is too low "
                                     "(min 2)", plant.get_name())
                if sun > 12:
                    raise PlantError(f"Sunlight hours {sun} is too high "
                                     "(max 12)", plant.get_name())
                print(f"{plant.get_name()}: healthy (water: "
                      f"{plant.get_water()}, sun: {plant.get_sun()})")
        except PlantError as e:
            print(f"Error checking {e.plant_name}: {e.msg}")


print("=== Garden Management System ===")
manager = GardenManager()

print("\nAdding plants to garden...")
manager.add_plant(Plant("tomato", 1, 8))
manager.add_plant(Plant("lettuce", 15, 8))
manager.add_plant(Plant("", 51, 20))

print("\nWatering plants...")
manager.water_plants()

print("\nChecking plant health...")
manager.check_health()

print("\nTesting error recovery...")
try:
    raise GardenError("Not enough water in tank")
except GardenError as e:
    print(f"Caught GardenError: {e.msg}")
finally:
    print("System recovered and continuing...")

print("\nGarden management system test complete!")
