from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DonationCreate(BaseModel):
    name: str
    email: str
    amount: float
    message: Optional[str] = ""

class DonationOut(DonationCreate):
    id: str
    created_at: datetime
