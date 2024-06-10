import unittest
from cart import ShoppingCart, Item

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        self.item1 = Item("Laptop", 1000)
        self.item2 = Item("Smartphone", 500)
        self.item3 = Item("Headphones", 100)

    def test_add_item(self):
        self.cart.add_item(self.item1)
        self.assertIn(self.item1, self.cart.items)
        self.cart.add_item(self.item2)
        self.assertIn(self.item2, self.cart.items)

    def test_remove_item(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.remove_item(self.item1)
        self.assertNotIn(self.item1, self.cart.items)
        self.cart.remove_item(self.item2)
        self.assertNotIn(self.item2, self.cart.items)

    def test_view_items(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.assertEqual(self.cart.view_items(), ["Laptop", "Smartphone"])
        self.cart.add_item(self.item3)
        self.assertEqual(self.cart.view_items(), ["Laptop", "Smartphone", "Headphones"])

    def test_total_price(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.assertEqual(self.cart.total_price(), 1500)
        self.cart.add_item(self.item3)
        self.assertEqual(self.cart.total_price(), 1600)

    def test_total_price_2(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.add_item(self.item3)
        self.assertEqual(self.cart.total_price(), 1600)
        self.cart.remove_item(self.item3)
        self.assertEqual(self.cart.total_price(), 1400)  ######## should be 1500


if __name__ == '__main__':
    unittest.main()
