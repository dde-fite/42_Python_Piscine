class Plant:
    """A class representing a Plant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
    """

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
        """
        self.__name: str = name
        self.__height: int = height

    def get_name(self) -> str:
        """Returns the name of the Plant."""
        return self.__name

    def get_height(self) -> int:
        """Returns the height of the Plant."""
        return self.__height

    def set_name(self, name: str) -> None:
        """Sets the name of the Plant."""
        self.__name = name

    def set_height(self, height: int) -> None:
        """Sets the height of the Plant."""
        self.__height = height

    def grow_plant(self, height: int = 1) -> None:
        """Increases the value of the plant by the value provided

        Args:
            height (int, optional): Height to increase in cm. Defaults to 1.
        """
        self.__height += height
        print(f"{self.__name} grew {height}cm")

    def print_data(self) -> None:
        print(f"{self.__name}: {self.__height}cm", end='')


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flowers: str,
                 is_blooming: bool) -> None:
        super().__init__(name, height)
        self.__flowers = flowers
        self.__is_blooming = is_blooming

    def get_flowers(self) -> str:
        """Returns the flowers of the FloweringPlant."""
        return self.__flowers

    def set_flowers(self, flowers: str) -> None:
        """Sets the flowers of the FloweringPlant."""
        self.__flowers = flowers

    def get_blooming(self) -> bool:
        """Returns the blooming state of the FloweringPlant."""
        return self.__is_blooming

    def set_blooming(self, is_blooming: bool) -> None:
        """Sets the blooming state of the FloweringPlant."""
        self.__is_blooming = is_blooming

    def print_data(self) -> None:
        super().print_data()
        print(f", {self.__flowers}", end='')
        if self.__is_blooming:
            print(" (blooming)", end='')


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, flowers: str,
                 is_blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, flowers, is_blooming)
        self.__prize_points = prize_points

    def get_prize_points(self) -> int:
        return self.__prize_points

    def set_prize_points(self, prize_points: int) -> None:
        self.__prize_points = prize_points

    def print_data(self) -> None:
        super().print_data()
        print(f", Prize points: {self.__prize_points}", end='')


class Garden():
    def __init__(self, name: str, owner: str) -> None:
        self.__name: str = name
        self.__owner: str = owner
        self.__plants: list[Plant | FloweringPlant | PrizeFlower] = []
        self.__growth = 0

    def get_name(self) -> str:
        """Returns the name of the Garden."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Sets the name of the Garden."""
        self.__name = name

    def add_plant(self, plant: Plant | FloweringPlant | PrizeFlower) -> None:
        self.__plants.append(plant)
        print(f"Added {plant.get_name()} to {self.__name}")

    def remove_plant(self, plant: Plant | FloweringPlant | PrizeFlower
                     ) -> None:
        self.__plants.remove(plant)

    def get_plants(self) -> list[Plant | FloweringPlant | PrizeFlower]:
        return self.__plants.copy()

    def grow_plants(self) -> None:
        print(f"\n{self.__owner} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow_plant()
        self.__growth += 1

    def print_stats(self) -> None:
        count: int = 0
        print("Plants in garden:")
        for plant in self.__plants:
            print("- ", end='')
            plant.print_data()
            print("")
            count += 1
        print(f"\nPlants added: {count}, Total growth: {self.__growth}\n")
            #   f"Plants types: {self.__plants.count(Plant)} regular")


class GardenManager():
    _gardens: list[Garden] = []

    @classmethod
    def create_garden(cls, name: str, owner: str) -> Garden:
        garden = Garden(name, owner)
        cls._gardens.append(garden)
        return garden

    @classmethod
    def remove_garden(cls, garden: Garden) -> None:
        cls._gardens.remove(garden)

    @classmethod
    def get_gardens(cls) -> list[Garden]:
        return cls._gardens.copy()

    @staticmethod
    def cap_words(s: str) -> str:
        words = s.split()
        for i in words:
            s = s.replace(i, i.capitalize())
        return s

    # @classmethod
    # def get_garden_by_name(cls, name: str) -> Garden | None:
    #     for garden in cls.__gardens:
    #         if garden.name == name:
    #             return garden
    #     return None

    class GardenStats():

        @staticmethod
        def print_stats(garden: Garden) -> None:
            print(f"\n=== {GardenManager.cap_words(garden.get_name())} "
                  "Report ===")
            garden.print_stats()


print("=== Garden Management System Demo ===\n")
garden = GardenManager.create_garden("Alice's garden", "Alice")
garden.add_plant(Plant("Oak Tree", 100))
garden.add_plant(FloweringPlant("Rose", 25, "red flowers", True))
garden.add_plant(PrizeFlower("Sunflower", 51, "yellow flowers", True, 10))
garden.grow_plants()
GardenManager.GardenStats.print_stats(garden)
