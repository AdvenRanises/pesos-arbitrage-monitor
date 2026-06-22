from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class PriceData(BaseModel):
    ticker: str
    price_usd: float = Field(gt=0, description="The asset price in USD")
    price_converted: float = Field(gt=0, description="The asset price in target currency")
    currency: str = Field(default="PHP", description="Target currency code (ISO 4217)")
    timestamp: datetime

    @field_validator('ticker')
    @classmethod
    def uppercase_ticker(cls, value: str) -> str:
        return value.upper()

    @field_validator('currency')
    @classmethod
    def uppercase_currency(cls, value: str) -> str:
        return value.upper()
