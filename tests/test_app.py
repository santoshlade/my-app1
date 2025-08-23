import unittest
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
