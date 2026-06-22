from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class PriceData(BaseModel):
    ticker: str
    price_usd: float = Field(gt=0, description="The asset price must be greater than zero")
    price_php: float = Field(gt=0, description="The asset price converted to Philippine Pesos")
    timestamp: datetime

    @field_validator('ticker')
    @classmethod
    def uppercase_ticker(cls, value: str) -> str:
        return value.upper()
