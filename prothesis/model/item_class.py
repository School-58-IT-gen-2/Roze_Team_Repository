class Item:
    def __init__(self, id, name, type='health', value=0, item_class='item', price=0):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.item_class = item_class
        self.price = price