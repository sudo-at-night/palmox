login_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "minLength": 3, "format": "email"},
        "password": {"type": "string", "minLength": 3},
    },
    "required": ["email", "password"],
}

register_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "minLength": 3, "format": "email"},
        "password": {"type": "string", "minLength": 3},
    },
    "required": ["email", "password"],
}
