
import os
from time import sleep
from dotenv import load_dotenv


load_dotenv()


print(228)
print("alpha")
if __name__ == "__mainv2__":
    secret_key = os.getenv("super_secret")
    print(secret_key)
    sleep(2)

    