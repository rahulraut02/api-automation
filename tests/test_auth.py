from data.booking_data import booking_payload


def test_auth_returns_token(api_client):
    response = api_client.post(
        "/auth",
        payload={"username": "admin", "password": "password123"},
    )

    assert response.status_code == 200, response.text
    assert isinstance(response.json().get("token"), str)
    assert response.json()["token"]


def test_patch_is_rejected_without_token(api_client):
    create_response = api_client.post(
        "/booking", payload=booking_payload()
    )
    assert create_response.status_code == 200, create_response.text
    booking_id = create_response.json()["bookingid"]

    response = api_client.patch(
        f"/booking/{booking_id}",
        payload={"firstname": "Changed"},
    )

    assert response.status_code == 403, response.text
