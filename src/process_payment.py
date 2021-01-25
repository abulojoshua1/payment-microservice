import requests
from flask_api import status
from requests.exceptions import ConnectionError

from src import app


class PremiumPaymentGateway:
    def __init__(self):
        try:
            response = requests.get(
                app.config["PREMIUM_PAYMENT_GATEWAY_URI"]
            )
            self.payment = (
                f"PremiumPaymentGateway: {response.json}",
                response.status_code,
            )
        except ConnectionError:
            self.payment = (
                "PremiumPaymentGateway: failed to process payment.",
                status.HTTP_400_BAD_REQUEST,
            )


class ExpensivePaymentGateway:
    def __init__(self):
        try:
            response = requests.get(
                app.config["EXPENSIVE_PAYMENT_GATEWAY_URI"]
            )
            self.payment = (
                f"ExpensivePaymentGateway: {response.json}",
                response.status_code,
            )
        except ConnectionError:
            self.payment = (
                "ExpensivePaymentGateway: failed to process payment.",
                status.HTTP_400_BAD_REQUEST,
            )


class CheapPaymentGateway:
    def __init__(self):
        try:
            response = requests.get(
                app.config["CHEAP_PAYMENT_GATEWAY_URI"]
            )
            self.payment = (
                f"CheapPaymentGateway: {response.json}",
                response.status_code,
            )
        except ConnectionError:
            self.payment = (
                "CheapPaymentGateway: failed to process payment.",
                status.HTTP_400_BAD_REQUEST,
            )


class ProcessPayment:
    def __init__(
        self, amount, card_holder,
        expiration_date, credit_card_number,
        security_code=None
    ):
        self.amount = amount
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.credit_card_number = credit_card_number

    def bill(self):
        if self.amount <= 20:
            return self.cheap_payment_gateway()
        elif 21 <= self.amount <= 500:
            return self.expensive_payment_gateway()
        else:
            return self.premium_payment_gateway()

    def cheap_payment_gateway(self):
        return CheapPaymentGateway()

    def expensive_payment_gateway(self):
        return ExpensivePaymentGateway()

    def premium_payment_gateway(self):
        return PremiumPaymentGateway()
