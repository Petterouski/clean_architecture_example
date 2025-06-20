class UseCases:
    def __init__(self, repository):
        self.repository = repository

    def add_item(self, item):
        self.repository.save(item)

    def get_items(self):
        return self.repository.load()