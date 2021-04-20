from argon2 import PasswordHasher

hasher = PasswordHasher(parallelism=2, hash_len=25, salt_len=25)
