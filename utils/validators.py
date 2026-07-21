from __future__ import annotations

import re

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

def validate_status_code(actual: int, expected: int) -> bool:
    return actual == expected

def validate_email(email: str) -> bool:
    return EMAIL_PATTERN.fullmatch(email) is not None

def validate_length(text: str, minimum: int, maximum: int) -> bool:
    return minimum <= len(text) <= maximum

def validate_not_empty(value: str) -> bool:
    return bool(value.strip())
