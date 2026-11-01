from datetime import date, timedelta


def booking_payload(
    firstname="Test",
    lastname="User",
    totalprice=150,
    depositpaid=True,
    checkin=None,
    nights=3,
    additionalneeds="Breakfast",
):
    checkin_date = checkin or date.today() + timedelta(days=7)
    checkout_date = checkin_date + timedelta(days=nights)

    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin_date.isoformat(),
            "checkout": checkout_date.isoformat(),
        },
        "additionalneeds": additionalneeds,
    }
