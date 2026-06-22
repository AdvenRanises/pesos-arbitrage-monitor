import pytest
from src.models import PriceData
from datetime import datetime, timezone

def test_price_data_conversion_logic():
    payload = {
        "ticker": "AAPL",
        "price_usd": 150.00,
        "price_php": 150.00 * 58.20,
        "timestamp": datetime.now(timezone.utc)
    }
    
    validated_data = PriceData(**payload)
    
    assert validated_data.ticker == "AAPL"
    assert validated_data.price_php == 8730.00

def test_ticker_uppercase_validation():
    payload = {
        "ticker": "aapl",
        "price_usd": 150.00,
        "price_php": 8730.00,
        "timestamp": datetime.now(timezone.utc)
    }
    
    validated_data = PriceData(**payload)
    assert validated_data.ticker == "AAPL"

def test_invalid_price_raises_validation_error():
    from pydantic import ValidationError
    
    with pytest.raises(ValidationError):
        PriceData(
            ticker="AAPL",
            price_usd=-10.00,
            price_php=-582.00,
            timestamp=datetime.now(timezone.utc)
        )
