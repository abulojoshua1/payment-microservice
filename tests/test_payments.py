from unittest import TestCase

import mock
from flask_api import status

from app import app


class TestPayments(TestCase):
    """
    Tests that application payment process route runs without crushing
    """
    def setUp(self):
        app.config["CHEAP_PAYMENT_GATEWAY_URI"] = \
            "http://test-cheap=payment-gateway"
        app.config["EXPENSIVE_PAYMENT_GATEWAY_URI"] = \
            "http://test-expensive=payment-gateway"
        app.config["PREMIUM_PAYMENT_GATEWAY_URI"] = \
            "http://test-premium=payment-gateway"
        self.app = app
        self.test_client = self.app.test_client()
        self.headers = {
            "Content-Type": "application/json"
        }
        self.data = {
            "amount": 1000,
            "card_holder": "paul pogba",
            "expiration_date": "2026-01-26",
            "security_code": "185",
            "credit_card_number": "340000000000009",
        }

    def test_that_get_method_not_allowed(self):
        response = self.test_client.get("/payments", headers=self.headers)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    @mock.patch("requests.post")
    def test_premium_payment_gateway(self, mock_request):
        mock_request.return_value.status_code = status.HTTP_200_OK
        response = self.test_client.post(
            "/payments", headers=self.headers, json=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @mock.patch("requests.post")
    def test_expensive_payment_gateway(self, mock_request):
        self.data["amount"] = 200
        mock_request.return_value.status_code = status.HTTP_200_OK
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @mock.patch("requests.post")
    def test_cheap_payment_gateway(self, mock_request):
        self.data["amount"] = 10
        mock_request.return_value.status_code = status.HTTP_200_OK
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_failed_premium_payment_gateway(self):
        self.data["amount"] = 1000
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_failed_expensive_payment_gateway(self):
        self.data["amount"] = 400
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_failed_cheap_payment_gateway(self):
        self.data["amount"] = 20
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDataValidation(TestCase):
    """
    Tests for data validation
    """
    def setUp(self):
        self.app = app
        self.test_client = self.app.test_client()
        self.headers = {
            "Content-Type": "application/json"
        }

    def test_that_negative_amounts_are_invalid(self):
        """
        Test that negative numbers are invalid amounts
        """
        data = {
            "amount": -1000,
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["amount"], ["min value is 0"])

    def test_that_non_float_or_integer_amounts_are_invalid(self):
        """
        Test that non integer/float values are invalid amounts
        """
        data = {
            "amount": "$o*£ggtt",
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["amount"], ["must be of float type"])

    def test_that_amount_is_required(self):
        """
        Test that amount is required
        """
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["amount"], ["required field"])

    def test_that_integer_card_holder_is_invalid(self):
        """
        Test that integer type is an invalid card holder
        """
        data = {
            "card_holder": 12345,
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["card_holder"],
                         ["must be of string type"])

    def test_that_card_holder_is_required(self):
        """
        Test that card holder is required
        """
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["card_holder"], ["required field"])

    def test_that_expiration_date_should_be_a_valid_data(self):
        """
        Test that expiration date should be a valid date
        """
        data = {
            "expiration_date": "ns-hsh-726"
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("time data 'ns-hsh-726' "
                      "does not match format '%Y-%m-%d'",
                      response.json["expiration_date"][0])
        self.assertEqual(response.json["expiration_date"][1],
                         "must be of datetime type")

    def test_that_expired_cards_cannot_be_billed(self):
        """
        Test that expired cards cannot be billed
        """
        data = {
            "expiration_date": "2015-01-26"
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Cannot bill an expired card.",
                      response.json["expiration_date"][0])
        self.assertEqual(response.json["expiration_date"][1],
                         "must be of datetime type")

    def test_that_expiration_date_is_required(self):
        """
        Test that expiration_date is required
        """
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json={})
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["expiration_date"], ["required field"])

    def test_invalid_credit_card_number(self):
        """
        Test that invalid credit cards numbers cannot be billed
        """
        data = {
            "credit_card_number": "invalid-card-number"
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_that_credit_card_number_is_required(self):
        """
        Test that credit card numbers are required
        """
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json={})
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json["credit_card_number"],
                         ["required field"])

    def test_that_security_code_should_have_a_length_of_three(self):
        """
        Test that security code should contain 3 characters
        """
        data = {
            "security_code": "12345"
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(" Invalid security code.",
                      response.json["security_code"][0])

    def test_that_security_code_should_contain_only_integers(self):
        """
        Test that security code should contain integer values
        """
        data = {
            "security_code": "xyz"
        }
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json=data)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid security code.",
                      response.json["security_code"][0])

    def test_that_security_code_is_not_required(self):
        """
        Test that expiration_date is required
        """
        response = self.test_client.post("/payments",
                                         headers=self.headers,
                                         json={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(
            bool(response.json.get("security_code"))
        )
