def ft_garden_summary():
    """
    Ask the user for the name of the garden and the number of plants, and \
    print that data along with a static status message.
    """
    name = input("Enter garden name: ")
    number = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {number}")
    print("Status: Growing well!")
