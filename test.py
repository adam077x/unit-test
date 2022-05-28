import unittest
import requests

class MainTest(unittest.TestCase):
    def test_add(self):
        r = requests.get("http://127.0.0.1:5000/test")

        self.assertEqual(r.text, "Test!")

if __name__ == "__main__":
    unittest.main()