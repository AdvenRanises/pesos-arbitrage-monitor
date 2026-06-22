import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from src.config import API_KEY, EXCHANGE_RATES
from src.models import PriceData
from datetime import datetime, timezone

class PriceFetcher:
    def __init__(self):
        self.base_url = "https://api.twelvedata.com/price"

    @retry(
        stop=stop_after_attempt(3), 
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    def fetch_ticker(self, ticker: str, currency: str = "PHP") -> PriceData:
        """Fetches asset price and converts to specified currency."""
        params = {
            "symbol": ticker,
            "apikey": API_KEY
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        raw_data = response.json()
        
        if "price" not in raw_data:
            raise KeyError(f"Invalid API response structure for ticker {ticker}: {raw_data}")
            
        price_usd = float(raw_data["price"])
        rate = EXCHANGE_RATES.get(currency.upper(), 58.20)
        
        return PriceData(
            ticker=ticker,
            price_usd=price_usd,
            price_converted=price_usd * rate,
            currency=currency,
            timestamp=datetime.now(timezone.utc)
        )
