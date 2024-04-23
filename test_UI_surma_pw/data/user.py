from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None
    confirm_password: str = None
