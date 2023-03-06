from unittest import TestCase

from domain.product import Sulfura
from domain.quality import Quality


class TestSulfura(TestCase):

    def test_sulfura_cannot_be_spoiled(self):
        a_sulfura = Sulfura(
            quality=Quality(10)
        )

        a_sulfura.spoil()

        assert a_sulfura.quality.value == 10
