import unittest

from Mod4.Task2.wtforms_validators_adv import app


class TestWtformsValidatorsAdv(unittest.TestCase):

    valid_data = {
            'email': 'valid_email@example.com',
            'phone': '1234567890',
            'name': 'Test Name',
            'address': 'Test Address',
            'index': '123456',
            'comment': 'Test Comment'
    }
    invalid_data = {
            'email': 'invalid_email',
            'phone': '12345678909331',
            'name': '',
            'address': '',
            'index': '123456WDWDD',
            'comment': 'Test Comment'
    }

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False  # Отключаем CSRF для тестирования
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = self.valid_data.copy()

    def test_valid_email(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        self.data['email'] = self.invalid_data['email']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('email' in response_text)

    def test_valid_phone(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        self.data['phone'] = self.invalid_data['phone']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('phone' in response_text)

    def test_valid_name(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        self.data['name'] = self.invalid_data['name']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response_text)

    def test_valid_address(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_address(self):
        self.data['address'] = self.invalid_data['address']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('address' in response_text)

    def test_valid_index(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_index(self):
        self.data['index'] = self.invalid_data['index']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('index' in response_text)

    # comment - Always be valid


if __name__ == '__main__':
    unittest.main()