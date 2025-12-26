def ft_harvest_total(harvest: int = 0):
    """
    Ask the user for the daily harvest for 3 days and print the total harvest.

    Args:
        harvest (int, optional): Initial harvest quantity. Defaults to 0.
    """
    for i in (1, 2, 3):
        harvest += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {harvest}")
