def ft_harvest_total(harvest: int = 0):
    for i in (1, 2, 3):
        harvest += int(input(f"Day {i} harvest: "))
    print("Total harvest:", harvest)
