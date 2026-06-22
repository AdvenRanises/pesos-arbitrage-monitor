import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWELVEDATA_API_KEY")
USD_TO_PHP = float(os.getenv("EXCHANGE_RATE_USD_PHP", 58.20))

if not API_KEY:
    raise ValueError("CRITICAL CONFIGURATION ERROR: TWELVEDATA_API_KEY is missing from the environment configuration.")
