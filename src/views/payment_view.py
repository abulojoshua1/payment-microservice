from flask_api import status

from src import app
from src.decorators import validate_json
from src.process_payment import ProcessPayment
from src.validate_schema import ValidationSchema


@app.route("/payments", methods=["POST"])
@validate_json(ValidationSchema.payment_details)
def process_payment(payment_credentials):
    payment = ProcessPayment(**payment_credentials)
    message, status_code = payment.bill().payment
    return { "message": message }, status_code
