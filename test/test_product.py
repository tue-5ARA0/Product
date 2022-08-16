from product import *


class TestProduct:
    def test_initialize_product(self):
        product = Product(1, 2)
        assert product.days_remaining == 1
        assert product.quality == 2

    def test_tick_fresh(self):
        # Quality for a fresh product is decreased by 1
        assert False

    def test_tick_past_due(self):
        # Quality for a product past due is decreased by 2
        assert False

    def test_tick_rotten(self):
        # Quality for a rotten product remains 0
        assert False
