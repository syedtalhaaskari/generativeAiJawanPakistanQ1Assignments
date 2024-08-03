import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"Price {price} must be greater or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} must be greater or equal to 0"
        
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.price * self.pay_rate
        
    def apply_increment(self, value):
        self.__price = self.price + self.price * value
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError("Name must be less than or equal to 10 characters long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    
    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                item.get('name'),
                float(item.get('price')),
                int(item.get('quantity'))
            )
        
    def __repr__(self):
        return f"""{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"""