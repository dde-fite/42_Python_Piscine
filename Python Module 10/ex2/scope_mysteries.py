from typing import Any, Callable


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def increase() -> int:
        nonlocal count
        count += 1
        return count
    return increase


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    count: int = initial_power

    def increase(power: int) -> int:
        nonlocal count
        count += power
        return count
    return increase


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        nonlocal memory
        memory[key] = value

    def recall(key: Any) -> Any:
        nonlocal memory
        return memory.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    increase = mage_counter()
    factory_flaming = enchantment_factory("Flaming")
    factory_frozen = enchantment_factory("Frozen")

    print(
        "\nTesting mage counter...\n"
        f"Call 1: {increase()}\n"
        f"Call 2: {increase()}\n"
        f"Call 3: {increase()}\n"

        "\nTesting enchantment factory...\n"
        f"{factory_flaming('Sword')}\n"
        f"{factory_frozen('Shield')}"
    )


if __name__ == "__main__":
    main()
