import sys
import time
from src.fetcher import PriceFetcher

def main():
    watch_list = ["AAPL", "MSFT", "BTC/USD"]
    currencies = ["PHP", "EUR", "JPY", "GBP"]
    fetcher = PriceFetcher()

    print("=== MULTI-CURRENCY ARBITRAGE MONITOR ===")

    for ticker in watch_list:
        print(f"\n--- {ticker} ---")
        for i, currency in enumerate(currencies):
            try:
                data = fetcher.fetch_ticker(ticker, currency)
                symbol = "₱" if currency == "PHP" else "€" if currency == "EUR" else "¥" if currency == "JPY" else "£"
                print(f"  [{data.timestamp.strftime('%H:%M:%S')}] {symbol}{data.price_converted:,.2f} {currency} (${data.price_usd:,.2f} USD)")
            except Exception as e:
                print(f"  FAILED {ticker}/{currency}: {str(e)}", file=sys.stderr)
            # Rate limit protection: sleep 1.5s between API calls
            if i < len(currencies) - 1:
                time.sleep(1.5)

if __name__ == "__main__":
    main()
