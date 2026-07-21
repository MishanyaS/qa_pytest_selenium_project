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