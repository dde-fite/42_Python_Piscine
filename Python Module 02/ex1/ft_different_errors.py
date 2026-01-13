def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        int("hi!")
    except ValueError as e:
        print(f"Caught ValueError: {e.args[0]}")

    print("\nTesting ZeroDivisionError...")
    try:
        50 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e.args[0]}")

    print("\nTesting FileNotFoundError...")
    try:
        with open("hih.dso") as file:
            print(file)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e.args[1]} '{e.filename}'")

    print("\nTesting KeyError...")
    try:
        test_dic = {"test1": True}
        print(test_dic["test2"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()

    print("\nTesting multiple errors together...")
    try:
        int("hi!")
        50 / 0
        with open("hih.dso") as file:
            print(file)
        test_dic = {"test1": True}
        print(test_dic["test2"])
    except:
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


test_error_types()
