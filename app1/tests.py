from django.test import TestCase
from rest_framework.test import APITestCase
from requests.auth import HTTPBasicAuth


# Create your tests here.
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "first_name": "admin", "last_name": "A", "emp_no":123
        }
        response = self.client.post("/empgv/", data)
        self.assertEqual(response.status_code, 201)