import math
import cmath
import utilities


def inputs():
    """
    takes valid user inputs and sets them to variables
    :return a, b, c: the user inputs
    """
    while True:
        # User inputs values for a, b, and c
        try:
            a = float(input("Enter a number for a: "))
            # Inf is an invalid input
            if math.isinf(a):
                print("Invalid input")
                quit()
            b = float(input("Enter a number for b: "))
            if math.isinf(b):
                print("Invalid input")
                quit()
            c = float(input("Enter a number for c: "))
            if math.isinf(c):
                print("Invalid input")
                quit()
        except ValueError:
            # Values that are not floats are invalid inputs
            print("Invalid input")
            quit()
        else:
            break
    return a, b, c


def discriminant(a, b, c):
    """
    finds the discriminant given the variables a, b, and c
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :return d: the discriminant
    """

    # Checks if the value of 'a' is zero
    utilities.check_a(a)
    try:
        # Computes discriminant
        d = float(b ** 2 - 4 * a * c)
        # Checks if discriminant is an integer in order to print correct form
        if d.is_integer():
            print("\nDiscriminant:", int(d))
        else:
            print("\nDiscriminant:", d)
        return d
    except OverflowError:
        # Checks if overflow occurs
        print("OVERFLOW ERROR")
        quit()


def quadratic_roots(a, b, c, d):
    """
    solves for the quadratic formula
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :param d: the discriminant
    """
    # Separate variables for print
    a_print, b_print, c_print = utilities.is_int(a, b, c)
    # Prints equation correctly based on values of b and c
    if b < 0 or c < 0 or b == 0 or c == 0:
        if b < 0 and c < 0:
            print("Equation: ", a_print, "x\u00B2 - ", -b_print, "x - ", -c_print, " = 0", sep="")
        elif (b < 0) and (c > 0):
            print("Equation: ", a_print, "x\u00B2 - ", -b_print, "x + ", c_print, " = 0", sep="")
        elif (c < 0) and (b > 0):
            print("Equation: ", a_print, "x\u00B2 + ", b_print, "x - ", -c_print, " = 0", sep="")
        elif b == 0 and c < 0:
            print("Equation: ", a_print, "x\u00B2 - ", -c_print, " = 0", sep="")
        elif b == 0 and c > 0:
            print("Equation: ", a_print, "x\u00B2 + ", c_print, " = 0", sep="")
        elif c == 0 and b < 0:
            print("Equation: ", a_print, "x\u00B2 - ", -b_print, "x = 0", sep="")
        elif c == 0 and b > 0:
            print("Equation: ", a_print, "x\u00B2 + ", b_print, "x = 0", sep="")
        else:
            print("Equation: ", a_print, "x\u00B2 = 0", sep="")
    else:
        print("Equation: ", a_print, "x\u00B2 + ", b_print, "x + ", c_print, " = 0", sep="")
    if d > 0:
        # Two roots will occur if discriminant is greater than zero
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        # Checks if roots are integers in order to display print statement correctly
        if root1.is_integer():
            root1 = int(root1)
        if root2.is_integer():
            root2 = int(root2)
        print("Two real roots found")
        print("x =", root1)
        print("x =", root2)
    elif d < 0:
        # One imaginary root will occur if discriminant is less than zero
        print("No real root(s) found")
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        print("Imaginary root found")
        # Formats print statement
        root_i = str(root1)
        root_i = root_i.replace("(", "")
        root_i = root_i.replace("j", "𝑖")
        root_i = root_i.replace(")", "")
        root_i = root_i.replace("+", " \u00B1 ")
        print("x =", root_i)
    else:
        # One root will occur if discriminant is equal to zero
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("One real root found")
        if root1.is_integer():
            root1 = int(root1)
        print("x =", root1)


def main():
    """
    runs program
    """
    print("\u2726 Quadratic Formula Calculator \u2726\n")
    a, b, c, = inputs()
    d = discriminant(a, b, c)
    quadratic_roots(a, b, c, d)


if __name__ == "__main__":
    main()
