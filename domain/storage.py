class Storage:

    def __init__(self, products):
        self.products = products or []

    def spoil(self):
        for product in self.products:
            product.spoil()
