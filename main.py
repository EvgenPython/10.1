class Hello:
    def __init__(self):
        super().__init__()
        self.word = "Word"
        self.name = "Oleg"

    def printU(self):
        print(self.name)


class Hi(Hello):
    def __init__(self):
        super().__init__()
        self.name = "Anna"
        self.age = 18

    def printU(self):
        print(self.name)


h = Hi()
print(h.age)
print(h.name)
print(h.word)
h.printU()


