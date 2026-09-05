import unittest

from app.services.greeting import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("suman"), "Hello, suman!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
