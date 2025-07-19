from fastapi import APIRouter, HTTPException
from app.models import DonationCreate
from app import crud

router = APIRouter()

@router.post("/donate")
async def donate(donation: DonationCreate):
    result = await crud.create_donation(donation)
    return {"message": "Donation successful", "donation": result}
