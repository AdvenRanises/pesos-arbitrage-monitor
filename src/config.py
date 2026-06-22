import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWELVEDATA_API_KEY")
if not API_KEY:
    raise ValueError("CRITICAL CONFIGURATION ERROR: TWELVEDATA_API_KEY is missing from the environment configuration.")

# Exchange rates relative to 1 USD
EXCHANGE_RATES = {
    "PHP": float(os.getenv("RATE_PHP", 58.20)),
    "EUR": float(os.getenv("RATE_EUR", 0.92)),
    "JPY": float(os.getenv("RATE_JPY", 157.50)),
    "GBP": float(os.getenv("RATE_GBP", 0.79)),
    "KRW": float(os.getenv("RATE_KRW", 1380.00)),
    "CNY": float(os.getenv("RATE_CNY", 7.24)),
}
