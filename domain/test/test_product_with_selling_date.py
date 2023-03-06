from unittest import TestCase

from domain.product_with_selling_date import ProductToSellIn
from domain.quality import Quality
from domain.sell_in_days import SellInDays


class TestProductWithSellingDate(TestCase):

    def test_can_get_sell_in_days(self):
        a_sell_in_days_value = SellInDays(10)
        a_product = ProductToSellIn(sell_in_days=a_sell_in_days_value)

        assert a_product.sell_in_days == a_sell_in_days_value

    def test_can_get_quality(self):
        a_quality = Quality(1)
        a_product = ProductToSellIn(quality=a_quality)

        assert a_product.quality == a_quality

    def test_product_can_spoil(self):
        an_initial_quality = Quality(5)
        an_initial_sell_in_days_value = SellInDays(4)
        a_product = ProductToSellIn(sell_in_days=an_initial_sell_in_days_value, quality=an_initial_quality)

        a_product.spoil()

        assert a_product.quality.value == 4
        assert a_product.sell_in_days.value == 3

    def test_when_sell_in_days_is_negative_then_product_is_spoiled_twice_faster(self):
        an_initial_quality = Quality(10)
        an_initial_sell_in_days_value = SellInDays(-1)
        a_product = ProductToSellIn(sell_in_days=an_initial_sell_in_days_value, quality=an_initial_quality)

        a_product.spoil()

        assert a_product.quality.value == 8
        assert a_product.sell_in_days.value == -2
