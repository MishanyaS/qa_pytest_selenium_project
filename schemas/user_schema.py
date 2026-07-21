USER_SCHEMA: dict = {
    "type": "object",
    "required": [
        "id",
        "firstName",
        "lastName",
        "email",
        "age",
        "gender",
    ],
    "properties": {
        "id": {
            "type": "integer",
        },
        "firstName": {
            "type": "string",
        },
        "lastName": {
            "type": "string",
        },
        "email": {
            "type": "string",
            "format": "email",
        },
        "age": {
            "type": "integer",
            "minimum": 0,
        },
        "gender": {
            "type": "string",
        },
    },
    "additionalProperties": True,
}