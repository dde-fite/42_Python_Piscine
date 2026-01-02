class SecurePlant:
    """
    A class representing a SecurePlant.

    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        age (int): Plant age in days
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a SecurePlant object.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            age (int): Plant age in days
        """
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Plant created: {self.__name}")

    def get_name(self):
        """
        Returns the name of the Plant.
        """
        return self.__name

    def get_height(self):
        """
        Returns the height of the Plant.
        """
        return self.__height

    def get_age(self):
        """
        Returns the age of the Plant.
        """
        return self.__age

    def set_height(self, height: int):
        """
        Sets a new value for height.

        Args:
            height (int): Height in cm.
        """
        if height < 0:
            print("\nInvalid operation attempted: height "
                  f"{height}cm [REJECTED]")
            self.security_exception("Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int):
        """
        Sets a new value for age.

        Args:
            age (int): Age in days.
        """
        if age < 0:
            print("\nInvalid operation attempted: age "
                  f"{age} days [REJECTED]")
            self.security_exception("Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days [OK]")

    def security_exception(self, msg: str = "There has been a "
                           "security exception."):
        """
        Broadcasts a security problem.

        Args:
            msg (str, optional): Message to broadcast. Defaults to "There has
            been a security exception.".
        """
        print(f"Security: {msg}\n")


print("=== Garden Security System ===")
plant1 = SecurePlant("Rose", 10, 5)
plant1.set_height(25)
plant1.set_age(30)
plant1.set_height(-5)
print(f"Current plant: {plant1.get_name()} ({plant1.get_height()}cm, "
      f"{plant1.get_age()})")
