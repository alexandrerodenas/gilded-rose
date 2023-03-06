class Quality:

    def __init__(self, value):
        self.value = value

    def decrease(self):
        self.value = max(self.value - 1, 0)

    def increase(self):
        self.value = min(self.value + 1, 50)

    def increase_by(self, increment):
        self.value = min(self.value + increment, 50)

    def divide_by_two(self):
        self.value /= 2
