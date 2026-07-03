#Secant is a root finding algorithm that uses two initial guesses.


def f(x):
    return x**3 - x -2

x0 = float(input("Enter first guess: "))      #secant 2 tahmin ister
x1 = float(input("Enter second guess: "))

tolerance = 0.0001     #hata toleransı 0'a yeterince yaklaşınca durması için
max_iterations = 100      #bir sorun çıkınca sonsuz döngüye girmemesi için
iteration = 0

while abs (f(x1)) > tolerance and iteration < max_iterations:
    denominator = f(x1) - f(x0)       #payda
    
    if denominator == 0:
        print("ERROR:Division by zero")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / denominator     #secant metodun asıl formülü
    x0 = x1
    x1 = x2

    iteration += 1

    print(f"\nIteration {iteration}")
    print(f"x = {x1:.6f}")
    print(f"f(x) = {f(x1):.6f}")
    
print(f"Approximate root: {x1:.6f}")
print(f"Iterations : {iteration}")
