##############################################################
##############################################################
######################### 1st Lesson #########################
######################### 11.05.2023 #########################
####################### Dorin Esinenco #######################
##############################################################
##############################################################

class cint:
    def __init__(self, value) -> None:
        if value < -999 or value > 999:
            raise ValueError("Object value out of permitted range -999..999")
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value


a = cint(20)
b = cint(10)

try:
    c = cint(1000)
except ValueError as e:
    print("[ERROR]:", e)
else:
    print("Object created successfully!")

print("Sum:\t\t\t", a + b)
print("Subtraction:\t\t", a - b)
print("Product:\t\t", a * b)
print("Division:\t\t", a / b)
print("a is greater than b:\t", a > b)
print("a is less than b:\t", a < b)
print("a is equal with b:\t", a == b)
b.value = a.value
print("a is equal with b:\t", a == b)
