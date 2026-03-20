from typing import Callable, Any
from time import time_ns
# from functools import wraps


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    def measure():
        print(f"Casting {func.__name__}...")
        start = time_ns()
        res = func()
        print(f"Spell com pleted in {(time_ns() - start) / 10000} seconds")
        return res
    return measure


def power_validator(min_power: int) -> Callable:
    pass


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")


if __name__ == "__main__":
    main()
