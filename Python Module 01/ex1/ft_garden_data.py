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


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===\n"
      f"{plant1.name}: {plant1.height}cm, {plant1.age} days old\n"
      f"{plant2.name}: {plant2.height}cm, {plant2.age} days old\n"
      f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
