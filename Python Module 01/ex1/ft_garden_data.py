class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"{self.name}: {self.height}cm, {self.age} days old")


# plant1 = Plant("Rose", 25, 30)
# plant2 = Plant("Sunflower", 80, 45)
# plant3 = Plant("Cactus", 15, 120)
