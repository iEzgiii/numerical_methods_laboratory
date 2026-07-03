print("Error Analysis")
print("--------------")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
expected = float(input("Enter expected result: "))

result = a + b
error = abs(expected - result)

print("\nFloating Point Error")
print(f"Calculated result: {result:.17f}")
print(f"Expected result: {expected:.17f}")
print(f"Absolute error: {error:.17f}")
print("\nError Propagation")

value = float(input("Enter a value to add repeatedly: "))
count = int(input("Enter repetition count: "))
total = 0.0

for i in range(count):
    total += value

expected_total = value * count
propagation_error = abs(expected_total - total)

print(f"Calculated total: {total:.17f}")
print(f"Expected total: {expected_total:.17f}")
print(f"Absolute error: {propagation_error:.17f}")
print()