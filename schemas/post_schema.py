POST_SCHEMA: dict = {
    "type": "object",
    "required": [
        "id",
        "title",
        "body",
        "userId",
        "tags",
        "reactions",
        "views",
    ],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1,
        },
        "title": {
            "type": "string",
            "minLength": 1,
        },
        "body": {
            "type": "string",
            "minLength": 1,
        },
        "userId": {
            "type": "integer",
            "minimum": 1,
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "reactions": {
            "type": "object",
            "required": [
                "likes",
                "dislikes",
            ],
            "properties": {
                "likes": {
                    "type": "integer",
                    "minimum": 0,
                },
                "dislikes": {
                    "type": "integer",
                    "minimum": 0,
                },
            },
        },
        "views": {
            "type": "integer",
            "minimum": 0,
        },
    },
    "additionalProperties": True,
}

CREATE_POST_SCHEMA: dict = {
    "type": "object",
    "required": [
        "id",
        "title",
        "body",
        "userId",
    ],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1,
        },
        "title": {
            "type": "string",
            "minLength": 1,
        },
        "body": {
            "type": "string",
            "minLength": 1,
        },
        "userId": {
            "type": "integer",
            "minimum": 1,
        },
    },
    "additionalProperties": True,
}