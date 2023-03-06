from domain.product import Product
from domain.quality import Quality
from domain.sell_in_days import SellInDays


class ProductToSellIn(Product):

    def __init__(self, quality=Quality(0), sell_in_days=SellInDays(0)):
        super().__init__(quality)
        self.sell_in_days = sell_in_days

    def spoil(self):
        self.sell_in_days.decrease()
        if self.sell_in_days.value < 0:
            self.quality.decrease()
            self.quality.decrease()
        else:
            self.quality.decrease()


class AgedBrie(ProductToSellIn):

    def spoil(self):
        self.sell_in_days.decrease()
        self.quality.increase()


class BackstagePass(ProductToSellIn):

    def spoil(self):
        self.sell_in_days.decrease()

        if self.sell_in_days.value > 10:
            self.quality.increase()
        elif self.sell_in_days.value > 5:
            self.quality.increase_by(2)
        elif self.sell_in_days.value > 1:
            self.quality.increase_by(3)
        else:
            self.quality = Quality(0)


class ConjuredProduct(ProductToSellIn):

    def spoil(self):
        self.sell_in_days.decrease()
        self.quality.divide_by_two()

