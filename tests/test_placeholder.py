from data.booking_data import booking_payload


PLACEHOLDER_PRICE = 9999


def is_placeholder_price(price):
    return price == PLACEHOLDER_PRICE


def test_booking_with_sentinel_price_is_flagged(api_client):
    payload = booking_payload(
        firstname="Placeholder",
        lastname="Check",
        totalprice=PLACEHOLDER_PRICE,
    )

    create_response = api_client.post("/booking", payload=payload)
    assert create_response.status_code == 200, create_response.text
    booking_id = create_response.json()["bookingid"]

    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 200, get_response.text

    stored_price = get_response.json()["totalprice"]
    assert stored_price == PLACEHOLDER_PRICE
    assert is_placeholder_price(stored_price), (
        f"Price {stored_price} is the configured placeholder value"
    )
