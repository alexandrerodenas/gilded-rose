from unittest import TestCase

from domain.product_with_selling_date import ConjuredProduct
from domain.quality import Quality
from domain.sell_in_days import SellInDays


class TestConjuredProduct(TestCase):

    def test_quality_of_conjured_product_decrease_twice_faster(self):
        a_quality = Quality(20)
        a_sell_in_days = SellInDays(20)
        a_conjured_product = ConjuredProduct(
            quality=a_quality,
            sell_in_days=a_sell_in_days
        )

        a_conjured_product.spoil()

        assert a_conjured_product.quality.value == 10
        assert a_conjured_product.sell_in_days.value == 19
