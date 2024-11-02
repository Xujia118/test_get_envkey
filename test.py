import os

secret_key = os.getenv("SECRET_KEY")

print(f"Secret key is {secret_key}") if secret_key else print("No key fetched")