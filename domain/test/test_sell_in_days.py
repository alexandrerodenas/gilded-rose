from unittest import TestCase

from domain.sell_in_days import SellInDays


class TestSellInDays(TestCase):

    def test_can_get_value(self):
        a_sell_in_days = SellInDays(1)

        assert a_sell_in_days.value == 1

    def test_sell_in_days_can_decreased(self):
        a_sell_in_days = SellInDays(1)

        a_sell_in_days.decrease()

        assert a_sell_in_days.value == 0