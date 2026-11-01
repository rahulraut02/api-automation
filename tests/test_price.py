from datetime import date, timedelta
from decimal import Decimal

from data.booking_data import booking_payload


def test_total_price_matches_nightly_rate_times_nights(api_client):
    nightly_rate = Decimal("89.95")
    nights = 4
    expected_price = nightly_rate * nights

    checkin = date.today() + timedelta(days=10)
    payload = booking_payload(
        firstname="Price",
        lastname="Check",
        totalprice=float(expected_price),
        depositpaid=True,
        checkin=checkin,
        nights=nights,
    )

    create_response = api_client.post("/booking", payload=payload)
    assert create_response.status_code == 200, create_response.text
    booking_id = create_response.json()["bookingid"]

    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 200, get_response.text

    actual_price = Decimal(str(get_response.json()["totalprice"]))
    assert actual_price == expected_price
