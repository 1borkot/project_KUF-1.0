from fastapi import APIRouter, Query
from app import crud

router = APIRouter()

@router.get("/history")
async def get_history(email: str = Query(..., description="Email to lookup donations")):
    donations = await crud.get_donations_by_email(email)
    return {"email": email, "donations": donations}
