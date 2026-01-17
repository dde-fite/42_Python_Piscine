import sys

argv: list[str] = sys.argv.copy()
argc: int = len(argv)

print("=== Command Quest ===")
print(f"Program name: {argv.pop(0)}")
if argc > 1:
    print(f"Arguments received: {argc - 1}")
    for arg in argv:
        print(f"Argument {argv.index(arg)}: {arg}")
else:
    print("No arguments provided!")
print(f"Total arguments: {argc}")
