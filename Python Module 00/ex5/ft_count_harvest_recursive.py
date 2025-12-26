def ft_count_harvest_recursive():
    """
    Ask the user how many days are left until harvest and print one line for \
    each day from the first to the last.

    This function uses recursion to operate.
    """
    def harvst_recursion(day: int):
        if day > 1:
            harvst_recursion(day - 1)
        print(f"Day {day}")
    days = int(input("Days until harvest: "))
    if days > 0:
        harvst_recursion(days)
    print("Harvest time!")
