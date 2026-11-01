from data.booking_data import booking_payload


def test_create_booking_and_read_all_fields(api_client):
    payload = booking_payload(
        firstname="Alex",
        lastname="Taylor",
        totalprice=275,
        depositpaid=False,
        additionalneeds="Late checkout",
    )

    create_response = api_client.post("/booking", payload=payload)
    assert create_response.status_code == 200, create_response.text
    booking_id = create_response.json()["bookingid"]
    assert isinstance(booking_id, int)

    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 200, get_response.text
    actual = get_response.json()

    assert actual["firstname"] == payload["firstname"]
    assert actual["lastname"] == payload["lastname"]
    assert actual["totalprice"] == payload["totalprice"]
    assert type(actual["totalprice"]) is int
    assert actual["depositpaid"] is payload["depositpaid"]
    assert type(actual["depositpaid"]) is bool
    assert actual["bookingdates"] == payload["bookingdates"]
    assert actual["additionalneeds"] == payload["additionalneeds"]
