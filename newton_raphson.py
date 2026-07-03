#Newton-Raphson uses an initial guess and the derivative of the function to find roots.


def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x = float(input("Enter guess(root): "))
tolerance = 0.0001
iteration = 0
max_iteration = 100

while abs(f(x)) > tolerance and iteration < max_iteration:
    x = x - (f(x) / df(x))
    iteration += 1

    print(f"\nIteration: {iteration}")
    print(f"x: {x:.6f}")
    print(f"f(x): {f(x):.6f}")

print(f"\nApproximate root: {x:.6f}")
print(f"\nIterations: {iteration}")