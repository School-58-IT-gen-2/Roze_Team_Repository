class Item:
    def __init__(self,  name,id, type='health', value=0,item_class='item', price=0):
        self.id = id
        self.name = name
        self.type = type
        self.item_class = item_class
        self.value = value
        self.price = price