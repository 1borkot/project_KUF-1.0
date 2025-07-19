from app.database import donation_collection
from app.models import DonationCreate
from datetime import datetime

async def create_donation(data: DonationCreate):
    doc = data.dict()
    doc["created_at"] = datetime.utcnow()
    result = await donation_collection.insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

async def get_donations_by_email(email: str):
    donations = []
    async for doc in donation_collection.find({"email": email}):
        doc["_id"] = str(doc["_id"])
        donations.append(doc)
    return donations
