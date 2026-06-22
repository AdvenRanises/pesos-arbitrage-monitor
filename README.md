# High-Resiliency Currency & Stock Arbitrage Monitor

A production-ready, object-oriented Python micro-utility designed to parse live international financial asset streams and accurately evaluate valuations mapped directly to Philippine Pesos (PHP).

## Key Engineering Features
* **Zero-Crash Resiliency:** Integrated with exponential backoff network retry strategies via `tenacity`.
* **Type-Safe Parsing:** Runtime data schema verification powered by `pydantic v2`.
* **Automated CI/CD:** Native testing pipeline running via GitHub Actions on every codebase mutation.

## Project Structure
* `src/` - Production modules (Configuration, Data Validation, Extractor).
* `tests/` - Robust isolated automated test blocks.

## Execution Matrix

### Prerequisites
Ensure you have Python 3.10+ installed and a valid API access token from [TwelveData](https://twelvedata.com).

### Local Initialization
1. Clone this repository.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Copy environment template:
```bash
cp .env.example .env
```
4. Edit `.env` with your real API key.

### Booting the Pipeline
```bash
python -m src.main
```

## Continuous Integration Verification
```bash
pytest
```

## Live Demo
Real-time multi-currency output:

```text
=== MULTI-CURRENCY ARBITRAGE MONITOR ===

--- AAPL ---
  [14:20:30] ₱17,534.79 PHP ($301.29 USD)
  [14:20:32] €277.04 EUR ($301.13 USD)
  [14:20:34] ¥47,427.97 JPY ($301.13 USD)
  [14:20:36] £237.90 GBP ($301.14 USD)

--- MSFT ---
  [14:20:37] ₱21,861.67 PHP ($375.63 USD)
  [14:20:40] €345.58 EUR ($375.63 USD)
  [14:20:48] ¥59,164.88 JPY ($375.65 USD)
  [14:20:52] £296.76 GBP ($375.65 USD)

--- BTC/USD ---
  [14:21:04] ₱3,788,142.55 PHP ($65,088.36 USD)
  [14:21:06] €59,882.48 EUR ($65,089.65 USD)
  [14:21:08] ¥10,252,678.28 JPY ($65,096.37 USD)
  [14:21:11] £51,416.49 GBP ($65,084.17 USD)
