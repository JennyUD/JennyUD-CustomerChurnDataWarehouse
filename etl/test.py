
import os


password = os.getenv("PG_PASSWORD")
print(f"Password from environment variable: {password}")