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
