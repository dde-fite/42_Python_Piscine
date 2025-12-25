def ft_count_harvest_recursive():
    def harvst_recursion(day: int):
        if day > 1:
            harvst_recursion(day - 1)
        print("Day", day)
    days = int(input("Days until harvest: "))
    if days > 0:
        harvst_recursion(days)
    print("Harvest time!")
