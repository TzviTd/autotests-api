import time

#function that creates unique email address using timestamp
def get_random_email() -> str:
    return f"time.{time.time()}@example.com"