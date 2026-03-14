from enum import Enum
from datetime import datetime
from pydantic import (BaseModel, Field, ValidationError,
                      model_validator)


class ContactType(Enum):
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    VISUAL = "visual"
    RADIO = "radio"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(values):
        if not values.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if (values.contact_type == ContactType.PHYSICAL
           and not values.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (values.contact_type == ContactType.TELEPATHIC
           and values.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3"
                             " witnesses")
        if (values.signal_strength > 7.0 and not values.message_received):
            raise ValueError("Strong signals (>7.0) must include a received"
                             " message")
        return values


def main():
    contact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        timestamp=datetime(2025, 1, 21)
    )
    print(
        "Alien Contact Log Validation\n"
        "======================================\n"
        "Valid contact report:\n"
        f"ID: {contact.contact_id}\n"
        f"Type: {contact.contact_type.value}\n"
        f"Location: {contact.location}\n"
        f"Signal: {contact.signal_strength}/10\n"
        f"Duration: {contact.duration_minutes} minutes\n"
        f"Witnesses: {contact.witness_count}\n"
        f"Message: '{contact.message_received}'\n"

        "\n======================================"
    )
    try:
        AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            timestamp=datetime(2025, 1, 21)
        )
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])


if __name__ == "__main__":
    main()
