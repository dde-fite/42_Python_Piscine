from typing import Any, Callable


def spell_combiner(spell1: Callable[..., Any], spell2: Callable[..., Any]
                   ) -> Callable[..., tuple[Any, Any]]:
    def combine(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combine


def power_amplifier(base_spell: Callable[..., int | float], multiplier: int
                    ) -> Callable[..., int | float]:
    def amplify(*args: Any, **kwargs: Any) -> int | float:
        return base_spell() * multiplier
    return amplify


def conditional_caster(condition: Callable[..., bool],
                       spell: Callable[..., Any]) -> Callable[..., Any]:
    def caster(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable[..., Any]]
                   ) -> Callable[..., list[Any]]:
    def sequencer(*args: Any, **kwargs: Any) -> list[Any]:
        result: list[Any] = []
        for s in spells:
            result.append(s(*args, **kwargs))
        return result
    return sequencer


def main() -> None:
    def fireball() -> str:
        return "Fireball hits Dragon"

    def heal() -> str:
        return "Heals Dragon"

    def waterball() -> int:
        return 10

    combined = spell_combiner(fireball, heal)
    mega_waterball = power_amplifier(waterball, 3)

    print(
        "\nTesting spell combiner...\n"
        f"Combined spell result: {', '.join(combined())}\n"

        "\nTesting power amplifier...\n"
        f"Original: {waterball()}, Amplified: {mega_waterball()}"

    )


if __name__ == "__main__":
    main()
