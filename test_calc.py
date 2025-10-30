import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calculator.clear_history()
        user_input = "5 + 3"
        calculator.calculate(user_input)
        with open(calculator.HISTORY_FILE, "r") as f:
            history = f.read().strip()
        self.assertIn("5 + 3", history)
        self.assertIn("8", history)

    def test_divide_by_zero(self):
        result = calculator.calculate("5 / 0")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        result = calculator.calculate("5 ^ 2")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
