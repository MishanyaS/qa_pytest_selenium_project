COMMENT_SCHEMA: dict = {
    "type": "object",
    "required": [
        "id",
        "body",
        "postId",
        "likes",
        "user",
    ],
    "properties": {
        "id": {
            "type": "integer",
        },
        "body": {
            "type": "string",
        },
        "postId": {
            "type": "integer",
        },
        "likes": {
            "type": "integer",
            "minimum": 0,
        },
        "user": {
            "type": "object",
            "required": [
                "id",
                "username",
            ],
            "properties": {
                "id": {
                    "type": "integer",
                },
                "username": {
                    "type": "string",
                },
            },
        },
    },
    "additionalProperties": True,
}

CREATE_COMMENT_SCHEMA: dict = {
    "type": "object",
    "required": [
        "body",
        "postId",
        "userId",
    ],
    "properties": {
        "body": {
            "type": "string",
            "minLength": 1,
        },
        "postId": {
            "type": "integer",
            "minimum": 1,
        },
        "userId": {
            "type": "integer",
            "minimum": 1,
        },
    },
    "additionalProperties": True,
}

CREATE_COMMENT_RESPONSE_SCHEMA: dict = {
    "type": "object",
    "required": [
        "id",
        "body",
        "postId",
        "user",
    ],
    "properties": {
        "id": {
            "type": "integer",
        },
        "body": {
            "type": "string",
        },
        "postId": {
            "type": "integer",
        },
        "user": {
            "type": "object",
            "required": [
                "id",
                "username",
            ],
            "properties": {
                "id": {
                    "type": "integer",
                },
                "username": {
                    "type": "string",
                },
                "fullName": {
                    "type": "string",
                },
            },
            "additionalProperties": True,
        },
    },
    "additionalProperties": True,
}