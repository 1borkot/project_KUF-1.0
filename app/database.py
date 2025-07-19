import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Get env vars with validation
MONGO_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URL or not DB_NAME:
    raise ValueError("Missing MongoDB configuration in .env file")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]  # Now guaranteed to be str
donation_collection = db["donations"]  # Also safe