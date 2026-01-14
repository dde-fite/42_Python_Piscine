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
        """Prints formatted data of the Plant"""
        print(f"{self.__name}: {self.__height}cm", end='')


class FloweringPlant(Plant):
    """A class representing a FloweringPlant, inheriting from Plant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        flowers (str): Description of the flowers
        is_blooming (bool): Blooming state
    """
    def __init__(self, name: str, height: int, flowers: str,
                 is_blooming: bool) -> None:
        """Initialize a FloweringPlant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            flowers (str): Description of the flowers
            is_blooming (bool): Blooming state
        """
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
        """Prints formatted data of the FloweringPlant"""
        super().print_data()
        print(f", {self.__flowers}", end='')
        if self.__is_blooming:
            print(" (blooming)", end='')


class PrizeFlower(FloweringPlant):
    """A class representing a PrizeFlower, inheriting from FloweringPlant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        flowers (str): Description of the flowers
        is_blooming (bool): Blooming state
        prize_points (int): Points awarded for this plant
    """
    def __init__(self, name: str, height: int, flowers: str,
                 is_blooming: bool, prize_points: int) -> None:
        """Initialize a PrizeFlower object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            flowers (str): Description of the flowers
            is_blooming (bool): Blooming state
            prize_points (int): Prize points awarded
        """
        super().__init__(name, height, flowers, is_blooming)
        self.__prize_points = prize_points

    def get_prize_points(self) -> int:
        """Returns the prize points of the PrizeFlower."""
        return self.__prize_points

    def set_prize_points(self, prize_points: int) -> None:
        """Sets the prize points of the PrizeFlower."""
        self.__prize_points = prize_points

    def print_data(self) -> None:
        """Prints formatted data of the PrizeFlower"""
        super().print_data()
        print(f", Prize points: {self.__prize_points}", end='')


class Garden():
    """A class representing a Garden containing plants.

    Attributes:
        name (str): Garden name
        owner (str): Owner of the garden
        score (int): Garden score
    """
    def __init__(self, name: str, owner: str, score: int = 0) -> None:
        """Initialize a Garden object.

        Args:
            name (str): Garden name
            owner (str): Garden owner
            score (int, optional): Initial score. Defaults to 0.
        """
        self.__name: str = name
        self.__owner: str = owner
        self.__plants: list[Plant | FloweringPlant | PrizeFlower] = []
        self.__growth = 0
        self.__score = score

    def get_name(self) -> str:
        """Returns the name of the Garden."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Sets the name of the Garden."""
        self.__name = name

    def get_owner(self) -> str:
        """Returns the owner of the Garden."""
        return self.__owner

    def set_owner(self, owner: str) -> None:
        """Sets the owner of the Garden."""
        self.__owner = owner

    def get_score(self) -> int:
        """Returns the score of the Garden."""
        return self.__score

    def add_plant(self, plant: Plant | FloweringPlant | PrizeFlower) -> None:
        """Adds a plant to the garden and increases the score.

        Args:
            plant: Plant instance to add
        """
        self.__plants.append(plant)
        self.__score += 55
        print(f"Added {plant.get_name()} to {self.__name}")

    def remove_plant(self, plant: Plant | FloweringPlant | PrizeFlower
                     ) -> None:
        """Removes a plant from the garden and decreases the score.

        Args:
            plant: Plant instance to remove
        """
        self.__plants.remove(plant)
        self.__score -= 60
        print(f"Removed {plant.get_name()} from {self.__name}")

    def get_plants(self) -> list[Plant | FloweringPlant | PrizeFlower]:
        """Returns a copy of the plants in the garden."""
        return self.__plants.copy()

    def grow_plants(self) -> None:
        """Grows all plants in the garden and updates growth and score."""
        print(f"\n{self.__owner} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow_plant()
            self.__growth += 1
            self.__score += 18

    def print_stats(self) -> None:
        """Prints statistics of the garden, including plant data and growth."""
        count: int = 0
        print("Plants in garden:")
        for plant in self.__plants:
            print("- ", end='')
            plant.print_data()
            print("")
            count += 1
        print(f"\nPlants added: {count}, Total growth: {self.__growth}cm")
        self.__print_plant_types()

    def __print_plant_types(self) -> None:
        """Prints the count of each plant type in the garden."""
        print("Plant types: ", end='')
        count_plant_type = GardenManager.count_plant_types_garden(self)
        i: int = 0
        for p_type in GardenManager.plant_types:
            if i == 0:
                print(f"{GardenManager.plant_types[p_type]}: ", end='')
            else:
                print(f", {GardenManager.plant_types[p_type]}: ", end='')
            print(count_plant_type[p_type.__name__], end='')
            i += 1
        print()


class GardenManager():
    """A manager class responsible for handling multiple gardens."""
    _gardens: list[Garden] = []
    _gardens_count: int = 0
    plant_types = {
        Plant: "regular",
        FloweringPlant: "flowering",
        PrizeFlower: "prize flowers"
    }

    @classmethod
    def create_garden(cls, name: str, owner: str, score: int = 0) -> Garden:
        """Creates a new garden and registers it.

        Args:
            name (str): Garden name
            owner (str): Garden owner
            score (int, optional): Initial score. Defaults to 0.

        Returns:
            Garden: The created garden
        """
        garden = Garden(name, owner, score)
        cls._gardens.append(garden)
        return garden

    def create_garden_network(cls, gardens_name: list[str], author: str
                              ) -> None:
        for garden in gardens_name:
            cls.create_garden(garden, author)

    @classmethod
    def remove_garden(cls, garden: Garden) -> None:
        """Removes a garden from the manager.

        Args:
            garden (Garden): Garden to remove
        """
        cls._gardens.remove(garden)

    @classmethod
    def get_gardens(cls) -> list[Garden]:
        """Returns a copy of all managed gardens."""
        return cls._gardens.copy()

    @staticmethod
    def count_plant_types_garden(garden: Garden) -> dict[str, int]:
        """Counts plant types inside a garden.

        Args:
            garden (Garden): Garden to analyze

        Returns:
            dict[str, int]: Dictionary with plant class names as keys
                            and their counts as values
        """
        new_dic = {}
        for plant in garden.get_plants():
            new_dic[plant.__class__.__name__] = 1
        return new_dic

    class GardenStats():
        """Utility class providing statistics and validations for gardens."""

        @staticmethod
        def is_valid_height(plants: list[Plant | FloweringPlant | PrizeFlower]
                            ) -> bool:
            """Checks if all plants have a valid (non-negative) height.

            Args:
                plants: List of plants to validate

            Returns:
                bool: True if all heights are valid, False otherwise
            """
            return all(not plant.get_height() < 0 for plant in plants)

        @staticmethod
        def cap_words(s: str) -> str:
            """Capitalizes the first letter of each word in a string.

            Args:
                s (str): Input string

            Returns:
                str: Capitalized string
            """
            words = s.split()
            for i in words:
                s = s.replace(i, i.capitalize())
            return s

        @staticmethod
        def print_scores(gardens: list[Garden]) -> None:
            """Prints the scores of all gardens.

            Args:
                gardens: List of gardens
            """
            print("Garden scores - ", end='')
            i: int = 0
            for garden in gardens:
                if i == 0:
                    print(f"{garden.get_owner()}: ", end='')
                else:
                    print(f", {garden.get_owner()}: ", end='')
                print(garden.get_score(), end='')
                i += 1
            print()

        @classmethod
        def print_stats(cls, garden: Garden) -> None:
            """Prints a full statistics report for a garden.

            Args:
                garden (Garden): Garden to generate the report for
            """
            print(f"\n=== {cls.cap_words(garden.get_name())} "
                  "Report ===")
            garden.print_stats()
            print("\nHeight validation test:",
                  cls.is_valid_height(garden.get_plants()))
            cls.print_scores(GardenManager.get_gardens())
            count: int = 0
            for _i in GardenManager.get_gardens():
                count += 1
            print(f"Total gardens managed: {count}")


print("=== Garden Management System Demo ===\n")
garden = GardenManager.create_garden("Alice's garden", "Alice")
GardenManager.create_garden("Bob's garden", "Bob", 92)
garden.add_plant(Plant("Oak Tree", 100))
garden.add_plant(FloweringPlant("Rose", 25, "red flowers", True))
garden.add_plant(PrizeFlower("Sunflower", 51, "yellow flowers", True, 10))
garden.grow_plants()
GardenManager.GardenStats.print_stats(garden)
