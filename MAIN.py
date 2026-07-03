
import subprocess
import sys
from pathlib import Path


# Folder where main.py is located
BASE_DIR = Path(__file__).parent


def run_file(filename):
    file_path = BASE_DIR / filename

    if not file_path.exists():
        print(f"\nError: {filename} was not found.")
        print("Please make sure the file is in the same folder as main.py.\n")
        return

    print(f"\nRunning {filename}...\n")
    subprocess.run([sys.executable, str(file_path)])
    print("\nProgram finished.")
    input("Press Enter to return to the main menu...")


def root_finding_menu():
    while True:
        print("\nRoot Finding Methods")
        print("1. Bisection Method")
        print("2. Newton-Raphson Method")
        print("3. Secant Method")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_file("bisection.py")
        elif choice == "2":
            run_file("newton_raphson.py")
        elif choice == "3":
            run_file("secant.py")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def interpolation_menu():
    while True:
        print("\nInterpolation Methods")
        print("1. Linear Interpolation")
        print("2. Cubic Spline Interpolation")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_file("linear_interpolation.py")
        elif choice == "2":
            run_file("cubic_spline_interpolation.py")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def differentiation_menu():
    while True:
        print("\nNumerical Differentiation Methods")
        print("1. Forward Difference")
        print("2. Backward Difference")
        print("3. Central Difference")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_file("forward_difference.py")
        elif choice == "2":
            run_file("backward_difference.py")
        elif choice == "3":
            run_file("central_difference.py")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def integration_menu():
    while True:
        print("\nNumerical Integration Methods")
        print("1. Trapezoidal Rule")
        print("2. Simpson's Rule")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_file("trapezoidal_rule.py")
        elif choice == "2":
            run_file("simpson_rule.py")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        print("\nNumerical Methods Laboratory")
        print("============================")
        print("1. Error Analysis")
        print("2. Root Finding")
        print("3. Interpolation")
        print("4. Numerical Differentiation")
        print("5. Numerical Integration")
        print("6. Linear Systems")
        print("7. LU Decomposition")
        print("8. Optimization")
        print("9. ODE Solver")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_file("error_analysis.py")
        elif choice == "2":
            root_finding_menu()
        elif choice == "3":
            interpolation_menu()
        elif choice == "4":
            differentiation_menu()
        elif choice == "5":
            integration_menu()
        elif choice == "6":
            run_file("linear_system.py")
        elif choice == "7":
            run_file("lu_decomposition.py")
        elif choice == "8":
            run_file("optimization.py")
        elif choice == "9":
            run_file("ode_solver.py")
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()