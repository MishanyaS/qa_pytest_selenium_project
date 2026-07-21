from __future__ import annotations

import random
import string
from typing import Any

def random_string(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits

    return "".join(random.choice(alphabet) for _ in range(length))

def random_email() -> str:
    return f"{random_string(12)}@example.com"

def is_positive(number: int | float) -> bool:
    return number > 0

def remove_none(data: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in data.items()
        if value is not None
    }


