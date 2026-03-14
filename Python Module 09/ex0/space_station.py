from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200, default=None)


def main() -> None:
    print(
        "Space Station Data Validation\n"
        "========================================"
    )
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2025, 1, 21),
        is_operational=True
    )
    print(
        "Valid station created:\n"
        f"ID: {station.station_id}\n"
        f"Name: {station.name}\n"
        f"Crew: {station.crew_size} people\n"
        f"Power: {station.power_level}%\n"
        f"Oxygen: {station.oxygen_level}%\n"
        f"Status: {'Operational' if station.is_operational else '[ERROR]'}\n"

        "\n========================================"
    )
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=54,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2025, 1, 21),
            is_operational=True
        )
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])


if __name__ == "__main__":
    main()
