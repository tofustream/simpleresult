import unittest
from simpleresult import Result


class TestResult(unittest.TestCase):
    def test_of_value(self):
        result = Result.success(42)
        self.assertEqual(result.value, 42)
        self.assertIsNone(result.error)
        self.assertFalse(result.has_error())

    def test_of_error(self):
        error_message = "An error occurred"
        result = Result.failure(error_message)
        self.assertIsNone(result.value)
        self.assertIsNotNone(result.error)
        self.assertEqual(result.error.message, error_message)
        self.assertTrue(result.has_error())


if __name__ == "__main__":
    unittest.main()
