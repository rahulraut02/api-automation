# API Automation

API tests for the Restful Booker service using Python, pytest and requests.

## Requirements

- Python 3.10 or later
- Internet connection

## Setup

Create a virtual environment:

**Windows**
```powershell
py -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the packages:

```bash
python -m pip install -r requirements.txt
```

The default API URL is `https://restful-booker.herokuapp.com`. To change it, copy
`.env.example` to `.env` and update the values.

## Run tests

Run all tests:

```bash
python -m pytest
```

Run one test file:

```bash
python -m pytest tests/test_booking.py
```

## Project structure

```text
api_automation/
├── api/
│   └── client.py
├── config/
│   └── settings.py
├── data/
│   └── booking_data.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_booking.py
│   ├── test_price.py
│   └── test_placeholder.py
├── .env.example
├── .gitignore
├── pytest.ini
└── requirements.txt
```

## Test coverage

- Check that valid credentials return an authentication token.
- Check that a PATCH request without a token is rejected.
- Create a booking, retrieve it and check the returned fields and data types.
- Check the booking price using the nightly rate and number of nights, including
  the decimal example `89.95 x 4`.
- Check that a total price of `9999` is reported as the placeholder value used
  in this assessment.

Each test creates its own booking. Tests do not rely on a fixed booking ID.

## Notes

The `9999` placeholder check is based on the rule in the assessment. The public
test API is shared and may occasionally be unavailable or reset its data.
