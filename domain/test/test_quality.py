from unittest import TestCase

from domain.quality import Quality


class TestQuality(TestCase):

    def test_quality_can_be_decreased(self):
        a_quality = Quality(1)

        a_quality.decrease()

        assert a_quality.value == 0

    def test_quality_can_be_increase(self):
        a_quality = Quality(1)

        a_quality.increase()

        assert a_quality.value == 2

    def test_quality_cannot_go_under_zero(self):
        a_quality = Quality(0)

        a_quality.decrease()

        assert a_quality.value == 0

    def test_quality_cannot_go_over_fifty(self):
        a_quality = Quality(50)

        a_quality.increase()

        assert a_quality.value == 50

    def test_quality_can_be_increased_by_a_number(self):
        a_quality = Quality(30)

        a_quality.increase_by(10)

        assert a_quality.value == 40

    def test_quality_can_be_divide_by_two(self):
        a_quality = Quality(30)

        a_quality.divide_by_two()

        assert a_quality.value == 15
