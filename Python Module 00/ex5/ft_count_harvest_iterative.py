def ft_count_harvest_iterative():
    """
    Ask the user how many days are left until harvest and print one line for \
    each day from the first to the last.

    This function uses loops to operate.
    """
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
