import unittest
from app import app

class FeedbackTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_categories_presence(self):
        response = self.app.get('/')
        # Ищем категорию, которая есть в списке 
        expected_text = 'Техподдержка'.encode('utf-8')
        self.assertIn(expected_text, response.data)

if __name__ == '__main__':
    unittest.main()