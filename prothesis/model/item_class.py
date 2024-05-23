class Item:
    def __init__(self, id, name, type='health', cls='item', value=0, price=0):
        self.id = id
        self.name = name
        self.type = type
        self.cls = cls
        self.value = value
        self.price = price