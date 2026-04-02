import unittest
from freezegun import freeze_time
from Mod2.Task4.hello_world_with_day import app


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_get_correct_username_with_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url+username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2024-02-13")
    def test_get_username_with_correct_weekday(self):
        username = "Анна"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        expected = f"Привет, {username}. Хорошего вторника!"
        self.assertEqual(response_text, expected)