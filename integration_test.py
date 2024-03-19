import unittest

import product
import shoppingCart
class TestShoppingCart(unittest.TestCase):

    def test_integration_shopping_cart(self):
        cart = shoppingCart.ShoppingCart()

        product1 = product.Product("Computer", 999.99, 2)
        product2 = product.Product("Phone", 599.99, 1)

        cart.addProduct(product1)
        cart.addProduct(product2)

        expected_total = product1.calculateTotal() + product2.calculateTotal()

        cart_total = cart.getCartTotal()
        self.assertEqual(cart_total, expected_total, "Incorrect total calculated")


if __name__ == '__main__':
    unittest.main()

