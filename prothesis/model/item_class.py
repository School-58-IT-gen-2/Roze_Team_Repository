class Item:
    def __init__(self, id, name, type='health', item_class='item',value=0, price=0):
        self.id = id
        self.name = name
        self.type = type
        self.item_class = item_class
        self.value = value
        self.price = price