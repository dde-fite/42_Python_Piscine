INITIAL_DAY = 1
DAYS_TO_GO = 6


class Plant:
    """
    A class representing a Plant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        age (int): Plant age in days
    """
    def __init__(self, name: str, height: int, days: int):
        """
        Initialize a Plant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            age (int): Plant age in days
        """
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def grow(self, height: int = 1):
        """
        Increases the height of the plant by the argument value

        Args:
            height (int, optional): Height in cm. Defaults to 1.
        """
        self.height += height

    def age(self, days: int = 1):
        """
        Increases the age of the plant by the argument value

        Args:
            days (int, optional): Age in days. Defaults to 1.
        """
        self.days += days

    def get_info(self):
        """
        Prints the data of the plant
        """
        print(f"{self.name}: {self.height}cm, {self.days} days old")


# Day 1
plant1 = Plant("Rose", 25, 30)
print(f"=== Day {INITIAL_DAY} ===")
plant1.get_info()
# Day 7
print(f"=== Day {INITIAL_DAY + DAYS_TO_GO} ===")
plant1.grow(DAYS_TO_GO)
plant1.age(DAYS_TO_GO)
plant1.get_info()
print(f"Growth this week: +{DAYS_TO_GO}cm")
