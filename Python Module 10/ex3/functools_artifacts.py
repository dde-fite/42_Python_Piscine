from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        raise ValueError("The spells list can not be empty!")
    ops: dict[str, Callable[..., int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[..., Any]
                      ) -> dict[str, Callable[..., Any]]:
    power = 50
    return {
        'fire_enchant': partial(base_enchantment, power, "fire_enchant"),
        'ice_enchant': partial(base_enchantment, power, "ice_enchant"),
        'lightning_enchant': partial(base_enchantment, power,
                                     "lightning_enchant")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 1:
        return 0
    if n < 3:
        return 1
    return (memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1))


def spell_dispatcher() -> Callable[..., str]:
    @singledispatch
    def dispatch(s: Any) -> str:
        return "Unknown operation"

    @dispatch.register(int)
    def _1(s: int) -> str:
        return f"Spelled {s} of damage"

    @dispatch.register(str)
    def _2(s: str) -> str:
        return f"Spelled {s} enchanment"

    @dispatch.register(list)
    def _3(s: list[Any]) -> str:
        string = ""
        for e in s:
            string += f"\n{dispatch(e)}"
        return string
    return dispatch


def common(power: int, element: str, target: str) -> str:
    return f"Applied {power} {element} to {target}"


def main() -> None:
    print(
        "\nTesting spell reducer...\n"
        f"Sum: {spell_reducer([23, 49, 19, 9], 'add')}\n"
        f"Product: {spell_reducer([60, 8, 24, 21], 'multiply')}\n"
        f"Max: {spell_reducer([23, 40, 19, 13], 'max')}\n"

        "\nTesting memoized fibonacci...\n"
        f"Fib(10): {memoized_fibonacci(10)}\n"
        f"Fib(15): {memoized_fibonacci(15)}"
    )


if __name__ == "__main__":
    main()
