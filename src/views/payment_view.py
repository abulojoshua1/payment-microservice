from flask_api import status

from src import app
from src.decorators import validate_json
from src.validate_schema import ValidationSchema


@app.route("/payments", methods=["POST"])
@validate_json(ValidationSchema.payment_details)
def process_payment(payment_credentials):
    # TODO -> add payment processing logic in this view
    return {
        "message": "Payment processed succefully"
    }, status.HTTP_200_OK
