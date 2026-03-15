from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artf: artf['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    powers: list[int] = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    artifacts = artifact_sorter([
        {'name': 'Fire Staff', 'power': 92, 'type': 'Depressive'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Estimulant'},
        {'name': 'heroin', 'power': 7, 'type': 'Depressive'},
        {'name': 'lsd', 'power': 12, 'type': 'Alucinating'},
    ])

    spells = spell_transformer(["fireball", "heal", "shield"])

    print(
        "\nTesting artifact sorter...\n"
        f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes before "
        f"{artifacts[1]['name']} ({artifacts[1]['power']} power)\n"

        "\nTesting spell transformer...\n"
        f"{' '.join(spells)}"
    )


if __name__ == "__main__":
    main()
