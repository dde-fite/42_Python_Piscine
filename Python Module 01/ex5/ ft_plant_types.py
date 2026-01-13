PI_NUMBER = 3.14159265358979323846264338327950288419716939937510582097494459230


class Plant:
    """A class representing a Plant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        age (int): Plant age in days
    """

    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            age (int): Plant age in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Subclass of Plant for representing a Flower.

    Attributes:
        name (str): Flower name
        height (int): Flower height in cm
        age (int): Flower age in days
        color (str): Flower color.
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        """Initializes a Flower object.

        Args:
            name (str): Flower name
            height (int): FLower height in cm
            age (int): Flower age in days
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Prints the blooming state of the Flower."""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """Subclass of Plant for representing a Tree.

    Attributes:
        name (str): Tree name
        height (int): Tree height in cm
        age (int): Tree age in days
        trunk_diameter (int): Tree diameter in cm.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initializes a Tree object.

        Args:
            name (str): Tree name
            height (int): Tree height in cm
            age (int): Tree age in days
            trunk_diameter (int): Tree diameter in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate the area of shade in square meters for an oak tree.

        The mathematical formula is an example that you cannot take seriously,
        but it seemed pointless to me to make the function display a
        predefined static value.

        0.7 is the average diameter of an adult Oak.
        """
        shade_len = (((0.7 * self.height / 100) / 2) ** 2) * PI_NUMBER
        print(f"{self.name} provides {shade_len} square meters of shade\n")


class Vegetable(Plant):
    """Subclass of Plant for representing a Vegetable.

    Attributes:
        name (str): Vegetable name
        height (int): Vegetable height in cm
        age (int): Vegetable age in days
        harvest_season (str): Vegetable harvest season.
        nutritional_value (str): Nutritional value of the vegetable.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        """Initializes a Vegetable object.

        Args:
            name (str): Vegetable name
            height (int): Vegetable height in cm
            age (int): Vegetable age in days
            harvest_season (str): Vegetable harvest season.
            nutritional_value (str): Nutritional value of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


rose = Flower("Rose", 25, 30, "red")
oak = Tree("Oak", 500, 1825, 50)
tomato = Vegetable("Tomate", 80, 90, "summer", "vitamin C")

print("=== Garden Plant Types ===\n\n"
      f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} "
      "color")
rose.bloom()
print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
      f"{oak.trunk_diameter}cm diameter")
oak.produce_shade()
print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
      f"{tomato.harvest_season} harvest\n"
      f"{tomato.name} is rich in {tomato.nutritional_value}")
