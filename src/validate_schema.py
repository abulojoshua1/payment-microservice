from src.utils import coerce_to_date, coerce_to_integer


class _ValidateSchema:
    @property
    def payment_details(self):
        return {
            "credit_card_number": {
                "type": "string",
                "required": True,
                "regex": r"^(?:"
                         r"(4[0-9]{12}(?:[0-9]{3})?)"  # Visa
                         r"|(5[1-5][0-9]{14})"  # MasterCard
                         r"|(6(?:011|5[0-9]{2})[0-9]{12})"  # Discover
                         r"|(3[47][0-9]{13})"  # AMEX
                         r"|(3(?:0[0-5]|[68][0-9])[0-9]{11})"  # Diners Club
                         r"|((?:2131|1800|35[0-9]{3})[0-9]{11})"  # JCB
                         r")$",
            },
            "card_holder": {
                "type": "string",
                "required": True,
            },
            "security_code": {
                "type": "integer",
                "required": False,
                "coerce": coerce_to_integer,
            },
            "amount": {
                "type": "float",
                "required": True,
                "min": 0,
            },
            "expiration_date": {
                "type": "datetime",
                "required": True,
                "coerce": coerce_to_date,
            }
        }


ValidationSchema = _ValidateSchema()
