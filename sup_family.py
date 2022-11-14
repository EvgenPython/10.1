class Computer:
    def __init__(self, model, price,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 128
        self.model = model
        self.price = price


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4K"

class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)
        print(self.model)
        print(self.price)

iphone = SmartPhone(model="Last", price = 1000)
iphone.print_info()