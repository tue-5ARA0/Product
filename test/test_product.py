import unittest
import product as p


class ProductTest(unittest.TestCase):
    def test_initialize_product(self):
        product = p.Product(1, 2)
        self.assertEqual(product.days_remaining, 1)
        self.assertEqual(product.quality, 2)

    def test_tick_fresh(self):
        # Quality for a fresh product is decreased by 1
        product = p.Product(2, 3)
        product.tick()
        self.assertEqual(product.days_remaining, 1)
        self.assertEqual(product.quality, 2)

    def test_tick_past_due(self):
        # Quality for a product past due is decreased by 2
        product = p.Product(0, 3)
        product.tick()
        self.assertEqual(product.days_remaining, -1)
        self.assertEqual(product.quality, 1)

    def test_tick_rotten(self):
        # Quality for a rotten product remains 0
        product = p.Product(2, 0)
        product.tick()
        self.assertEqual(product.days_remaining, 1)
        self.assertEqual(product.quality, 0)


if __name__ == '__main__':
    unittest.main()
