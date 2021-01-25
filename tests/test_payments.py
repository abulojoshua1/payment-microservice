from unittest import TestCase

from flask_api import status

from app import app


class TestPayments(TestCase):
    def setUp(self):
        self.app = app
        self.test_client = self.app.test_client()
        self.headers = {
            "Content-Type": "application/json"
        }

    def test_that_get_method_not_allowed(self):
        response = self.test_client.get("/payments", headers=self.headers)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_that_post_method_is_allowed(self):
        response = self.test_client.post("/payments", headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
