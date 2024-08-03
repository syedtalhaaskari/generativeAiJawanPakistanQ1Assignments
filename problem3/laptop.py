from item import Item

class Laptop(Item):
    pay_rate = 0.7

    def __init__(self, name: str, price: float, quantity: int, gpu = 1, port_count = 1):
        assert gpu >= 1, f"GPU {gpu} must be greater or equal to 1"
        assert port_count >= 1, f"Port Count {port_count} must be greater or equal to 1"
        
        super().__init__(name, price, quantity)
        self.gpu = gpu
        self.port_count = port_count