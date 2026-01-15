class GardenError(Exception):
    """Generic error for garden problems."""
    def __init__(self, msg: str):
        self.msg = msg


class PlantError(GardenError):
    """Error for problems with plants, inherited from GardenError"""
    def __init__(self, msg: str):
        self.msg = msg


class WaterError(GardenError):
    """Error for problems with water, inherited from GardenError"""
    def __init__(self, msg: str):
        self.msg = msg


print("=== Custom Garden Errors Demo ===")

print("\nTesting PlantError...")
try:
    raise PlantError("The tomato plant is wilting!")
except PlantError as e:
    print(f"Caught PlantError: {e.msg}")

print("\nTesting WaterError...")
try:
    raise WaterError("Not enough water in the tank!")
except WaterError as e:
    print(f"Caught WaterError: {e.msg}")

print("\nTesting catching all garden errors...")
try:
    raise PlantError("The tomato plant is wilting!")
except GardenError as e:
    print(f"Caught a garden error: {e.msg}")
try:
    raise WaterError("Not enough water in the tank!")
except GardenError as e:
    print(f"Caught a garden error: {e.msg}")

print("\nAll custom error types work correctly!")
