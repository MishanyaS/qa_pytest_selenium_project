from __future__ import annotations

from typing import Any

def get_value(data: dict[str, Any], key: str) -> Any:
    return data[key]

def key_exists(data: dict[str, Any], key: str) -> bool:
    return key in data

def nested_value(data: dict[str, Any], *keys: str) -> Any:
    value: Any = data

    for key in keys:
        value = value[key]
    
    return value


