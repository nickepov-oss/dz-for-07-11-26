import random


class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        operation = random.choice(["+", "-", "*"])

        if operation == "+":
            return self.num1 + self.num2
        elif operation == "-":
            return self.num1 - self.num2
        else:
            return self.num1 * self.num2

n = Numbers(125, 120)
print(n.calculate())