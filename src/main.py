import sys
from src.fetcher import PriceFetcher

def main():
    watch_list = ["AAPL", "BTC/USD", "MSFT"]
    fetcher = PriceFetcher()
    
    print("=== STARTING PESOS ARBITRAGE MONITOR ===")
    
    for ticker in watch_list:
        try:
            data = fetcher.fetch_ticker_in_pesos(ticker)
            print(f"[{data.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {data.ticker}: ₱{data.price_php:,.2f} PHP (${data.price_usd:,.2f} USD)")
        except Exception as e:
            print(f"FAILED TO FETCH {ticker}: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()
