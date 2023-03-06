from unittest import TestCase

from domain.product_with_selling_date import AgedBrie
from domain.quality import Quality


class TestAgedBrie(TestCase):

    def test_quality_increase_by_time(self):
        an_initial_quality = Quality(1)
        an_aged_brie = AgedBrie(quality=an_initial_quality)

        an_aged_brie.spoil()

        assert an_aged_brie.quality.value == 2
