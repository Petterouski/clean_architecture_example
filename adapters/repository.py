class Repository:
    def __init__(self):
        self.data = []

    def save(self, item):
        self.data.append(item)

    def load(self):
        return self.data