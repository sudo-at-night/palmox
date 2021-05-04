from argon2 import PasswordHasher
from dotenv import dotenv_values

config = dotenv_values(".env")

hasher = PasswordHasher(parallelism=int(config["ARGON_PARALLELISM"]), hash_len=25, salt_len=25)
