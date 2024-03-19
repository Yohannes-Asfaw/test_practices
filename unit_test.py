import unittest
import product

class TestProduct(unittest.TestCase):

    def test_calculateTotal(self):
        # Create a Product instance
        product = product.Product("Laptop", 999.99, 2)

        # Call the calculateTotal method
        total = product.calculateTotal()

        # Define the expected total
        expected_total = 999.99 * 2

        # Assert that the calculated total matches the expected total
        self.assertEqual(total, expected_total, "Incorrect total calculated")

if __name__ == '__main__':
    unittest.main()