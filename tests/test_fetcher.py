import pytest
from src.models import PriceData
from datetime import datetime, timezone

def test_price_data_multi_currency():
    payload = {
        "ticker": "AAPL",
        "price_usd": 150.00,
        "price_converted": 150.00 * 0.92,
        "currency": "EUR",
        "timestamp": datetime.now(timezone.utc)
    }
    
    validated_data = PriceData(**payload)
    assert validated_data.ticker == "AAPL"
    assert validated_data.currency == "EUR"
    assert validated_data.price_converted == 138.0

def test_ticker_and_currency_uppercase():
    payload = {
        "ticker": "aapl",
        "price_usd": 150.00,
        "price_converted": 8730.00,
        "currency": "php",
        "timestamp": datetime.now(timezone.utc)
    }
    
    validated_data = PriceData(**payload)
    assert validated_data.ticker == "AAPL"
    assert validated_data.currency == "PHP"

def test_invalid_price_raises_validation_error():
    from pydantic import ValidationError
    
    with pytest.raises(ValidationError):
        PriceData(
            ticker="AAPL",
            price_usd=-10.00,
            price_converted=-582.00,
            currency="PHP",
            timestamp=datetime.now(timezone.utc)
        )
