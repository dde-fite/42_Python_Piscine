class Plant:
    """
    A class representing a Plant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        age (int): Plant age in days
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            age (int): Plant age in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_name(self):
        """
        Returns the name of the Plant.
        """
        return self.name

    def get_height(self):
        """
        Returns the height of the Plant.
        """
        return self.height

    def get_age(self):
        """
        Returns the age of the Plant.
        """
        return self.age


def print_json(plants: list[Plant]):
    """
    Prints in JSON format the details of the plants.

    Args:
        plants (list[Plant]): Lists of Plants objects
    """
    print("{")
    for plant in plants:
        print(
            f'    "{plant.name}": '
            "{\n"
            f"        height: {plant.height},\n"
            f"        age: {plant.age}\n"
            "     },"
        )
    print("}")


def list_len(list: list[Plant]):
    """
    Returns the quantity of Plants in a list

    Args:
        list (list[Plant]): Lists of Plants objects

    Returns:
        int: Number of plants
    """
    len: int = 0
    for item in list:  # pyright: ignore[reportUnusedVariable]
        len += 1
    return len


plants: list[Plant] = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120),
]
print("=== Plant Factory Output ===")
print_json(plants)
print(f"\nTotal plants created: {list_len(plants)}")
