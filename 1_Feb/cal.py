class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Can't divide by zero."


cal = Calculator(10, 5)


print("Addition:", cal.add())
print("Subtraction:", cal.sub())
print("Multiplication:", cal.mul())
print("Division:", cal.div())


