USTH Advanced Programming with Python 2026
==================================

Nguyễn Bảo Tuấn
2511108

ex.1
import math

radious = float(input("Enter radious value"))
area = math.pi * radious ** 2

print(f"Your area = {area:.1f}")

ex.2
temperature = float(input("Enter youre temperature"))
fahrenhiet = (temperature * 9/5) + 32
print(f"Your F after convert ={fahrenhiet:.3f}")

ex.3
num = int(input("Enter a number? "))

if num < 2:
    print(num, "is a NOT prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is a NOT prime number")

ex.4
num = int(input("Enter a number? "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print(num, "is a perfect number")
else:
    print(num, "is a NOT perfect number")

ex.5
colors = ["Blue", "Yellow", "Black", "Red", "White"]

color = input("What is your favorite color? ").strip().lower()

if color in [c.lower() for c in colors]:
    index = [c.lower() for c in colors] .index(color)
    print("Your color is at index", index, "in my list")
else:
    print("Sorry, I could not find your color")

ex.6
range1 = range(0, 7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))

ex.7
def remove_dollar_sign(s):
    return s.replace("$", "")


print(remove_dollar_sign("$100"))
print(remove_dollar_sign("Price: $50"))

ex.8
def extract_even(l):
    result = []

    for num in l:
        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))

ex.9
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

ex.10
def get_divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


num = int(input("Enter a number: "))
print("Divisors:", get_divisors(num))

ex.11
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance:", distance)

ex.12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")


print_pattern(4, 5)
