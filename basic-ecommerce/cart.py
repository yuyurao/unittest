class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def view_items(self):
        return [item.name for item in self.items]

    def total_price(self):
        return sum(item.price for item in self.items)
