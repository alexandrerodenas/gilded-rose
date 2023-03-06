from unittest import TestCase

from domain.product_with_selling_date import BackstagePass
from domain.quality import Quality
from domain.sell_in_days import SellInDays


class TestBackstagePass(TestCase):

    def test_quality_increase_by_one_when_sell_in_days_higher_than_ten(self):
        a_sell_in_days_higher_than_ten = SellInDays(12)
        a_quality = Quality(1)
        a_backstage_pass = BackstagePass(
            quality=a_quality,
            sell_in_days=a_sell_in_days_higher_than_ten
        )

        a_backstage_pass.spoil()

        assert a_backstage_pass.quality.value == 2
        assert a_backstage_pass.sell_in_days.value == 11

    def test_quality_increase_by_two_when_sell_in_days_lower_or_equal_than_ten(self):
        a_sell_in_days_lower_or_equal_than_ten = SellInDays(9)
        a_quality = Quality(1)
        a_backstage_pass = BackstagePass(
            quality=a_quality,
            sell_in_days=a_sell_in_days_lower_or_equal_than_ten
        )

        a_backstage_pass.spoil()

        assert a_backstage_pass.quality.value == 3
        assert a_backstage_pass.sell_in_days.value == 8

    def test_quality_increase_by_three_when_sell_in_days_lower_or_equal_than_five(self):
        a_sell_in_days_lower_or_equal_than_ten = SellInDays(3)
        a_quality = Quality(1)
        a_backstage_pass = BackstagePass(
            quality=a_quality,
            sell_in_days=a_sell_in_days_lower_or_equal_than_ten
        )

        a_backstage_pass.spoil()

        assert a_backstage_pass.quality.value == 4
        assert a_backstage_pass.sell_in_days.value == 2

    def test_quality_is_set_to_zero_if_sell_in_days_equal_zero(self):
        a_sell_in_days_lower_or_equal_than_ten = SellInDays(1)
        a_quality = Quality(10)
        a_backstage_pass = BackstagePass(
            quality=a_quality,
            sell_in_days=a_sell_in_days_lower_or_equal_than_ten
        )

        a_backstage_pass.spoil()

        assert a_backstage_pass.quality.value == 0
        assert a_backstage_pass.sell_in_days.value == 0