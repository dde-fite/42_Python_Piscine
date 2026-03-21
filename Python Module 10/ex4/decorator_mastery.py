from typing import Callable, Any
from time import time_ns
from functools import wraps


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    def measure():
        print(f"Casting {func.__name__}...")
        start = time_ns()
        res = func()
        print(f"Spell completed in {(time_ns() - start) / 10000} seconds")
        return res
    return measure


def power_validator(min_power: int) -> Callable[..., Any]:
    def validator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def speller(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return speller


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) >= 3:
            return False
        return all(
            not (not c.isalpha() and c != ' ') for c in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


# @power_validator(10)
# def test_validator(power: int):
#     return f"yayy you have {power} power"


# @retry_spell(5)
# def raiser() -> None:
#     raiser.counter += 1
#     if raiser.counter <= 4:
#         raise Exception("ERROR")
#     return "awawawawaw"
# raiser.counter = 0


def main() -> None:
    mage = MageGuild()

    print("\nTesting spell timer...")
    print(
        f"Result: {fireball()}\n"

        f"\nTesting {type(mage).__name__}...\n"
        f"{mage.validate_mage_name('Nora')}\n"
        f"{mage.validate_mage_name('Nora 34')}\n"
        f"{mage.cast_spell('Lightning', 15)}\n"
        f"{mage.cast_spell('Lightning', 3)}"
    )


if __name__ == "__main__":
    main()
