def ft_water_reminder():
    """
    Ask the user how many days it has been since the plant was last watered \
    and print whether it needs to be watered.
    """
    if int(input("Days since last watering: ")) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
