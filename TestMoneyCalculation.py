import unittest
from MoneyCalculator import calculate_change

class TestCalculateChange(unittest.TestCase):
    
    def test_exact_change(self):
        # Test case 1: $19.99
        self.assertEqual(
            calculate_change(19.99),
            {
                '10 bill': 1,
                '5 bill': 1,
                '1 bill': 4,
                'quarter': 3,
                'dime': 2,
                'penny': 4
            }
        )
        
    def test_small_amount(self):
        # Test case 2: $0.41
        self.assertEqual(
            calculate_change(0.41),
            {
                'quarter': 1,
                'dime': 1,
                'nickel': 1,
                'penny': 1
            }
        )
        
    def test_large_amount(self):
        # Test case 3: $1234.56
        self.assertEqual(
            calculate_change(1234.56),
            {
                '100 bill': 12,
                '20 bill': 1,
                '10 bill': 1,
                '1 bill': 4,
                'quarter': 2,
                'nickel': 1,
                'penny': 1
            }
        )

    def test_zero_amount(self):
        # Test case 4: $0.00
        self.assertEqual(calculate_change(0.00), {})

    def test_rounding(self):
        # Test case 5: Test rounding with $0.999
        self.assertEqual(
            calculate_change(0.999),
            {'1 bill': 1}
        )

    def test_all_coins(self):
        # Test case 6: $0.99 - using all types of coins
        self.assertEqual(
            calculate_change(0.99),
            {
                'quarter': 3,
                'dime': 2,
                'penny': 4
            }
        )

    def test_exact_dollars(self):
        # Test case 7: $500.00 - only dollar bills
        self.assertEqual(
            calculate_change(500.00),
            {
                '100 bill': 5
            }
        )

    def test_floating_point_precision(self):
        # Test case 8: $0.30 - testing floating point precision
        self.assertEqual(
            calculate_change(0.30),
            {
                'quarter': 1,
                'nickel': 1
            }
        )

    def test_single_penny(self):
        # Test case 9: $0.01 - smallest possible amount
        self.assertEqual(
            calculate_change(0.01),
            {'penny': 1}
        )

    def test_fifty_bill_usage(self):
        # Test case 10: $55.55 - using fifty dollar bill
        self.assertEqual(
            calculate_change(55.55),
            {
                '50 bill': 1,
                '5 bill': 1,
                'quarter': 2,
                'nickel': 1
            }
        )

    def test_mixed_large_amount(self):
        # Test case 11: $999.99 - testing large mixed amount
        self.assertEqual(
            calculate_change(999.99),
            {
                '100 bill': 9,
                '50 bill': 1,
                '20 bill': 2,
                '5 bill': 1,
                '1 bill': 4,
                'quarter': 3,
                'dime': 2,
                'penny': 4
            }
        )

    def test_invalid_negative_amount(self):
        # Test case 12: testing negative amounts
        with self.assertRaises(ValueError):
            calculate_change(-10.00)

    def test_invalid_input_type(self):
        # Test case 13: Invalid input type
        with self.assertRaises(TypeError):
            calculate_change("10.00")

    def test_excessive_decimal_places(self):
        # Test case 14: Testing amount with more than 2 decimal places
        self.assertEqual(
            calculate_change(10.999),
            {
                '10 bill': 1,
                '1 bill': 1
            }
        )

# Run the tests
if __name__ == "__main__":
    unittest.main()