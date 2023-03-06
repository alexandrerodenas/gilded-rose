from domain.quality import Quality


class Product:
    def __init__(self, quality=Quality(0)):
        self.quality = quality

    def spoil(self):
        pass


class Sulfura(Product):
    pass

