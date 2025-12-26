def ft_plant_age():
    """
        Asks the user for the age of the plant in days and prints whether it \
        can be harvested or not.
    """
    if int(input("Enter plant age in days: ")) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
