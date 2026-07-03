#Bisection uses an interval ([a,b]) to find roots.a and b must have opposite signs.


def f(x):
    return x**3 - x - 2

a = float(input("Enter left endpoint: "))
b = float(input("Enter right endpoint: "))
mid = (a + b) / 2
iteration = 0


if f(a) * f(b) > 0:
    print("Invalid interval. No root in this range.")
else:
    while abs(f(mid)) > 0.0001:
        iteration += 1

        if f(a) * f(mid) < 0:
           b = mid
        else:
            a = mid
    
        mid = (a + b ) / 2

        print("\nIteration: ",iteration)
        print(f"Mid: {mid:.6f}")
        print(f"f(mid): {f(mid):.6f}")

    print(f"\nApproximate root: {mid:.6f}")
    print(f"\nf(root) = {f(mid):.6f}\n")