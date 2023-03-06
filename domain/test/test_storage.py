from unittest import TestCase

from domain.product_with_selling_date import ProductToSellIn
from domain.quality import Quality
from domain.sell_in_days import SellInDays
from domain.storage import Storage


class TestStorage(TestCase):

    def test_products_in_storage_can_spoil(self):
        a_sell_in_days = SellInDays(2)
        a_quality = Quality(3)
        a_product = ProductToSellIn(sell_in_days=a_sell_in_days, quality=a_quality)
        another_sell_in_days = SellInDays(1)
        another_quality = Quality(1)
        another_product = ProductToSellIn(sell_in_days=another_sell_in_days, quality=another_quality)
        a_storage = Storage(
            products=[a_product, another_product]
        )

        a_storage.spoil()

        assert a_product.quality.value == 2
        assert a_product.sell_in_days.value == 1
        assert another_product.quality.value == 0
        assert another_product.sell_in_days.value == 0
