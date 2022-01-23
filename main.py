import math
import cmath


def inputs():
    """
    takes valid user inputs and sets them to variables
    :return a, b, c: the user inputs
    """
    print("\u2726 Quadratic Formula Calculator \u2726\n")
    while True:
        try:
            a = float(input("Enter a number for a: "))
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
            print("Invalid input")
            quit()
        else:
            break
    return a, b, c


def check_a(a):
    """
    checks to see if 'a' is equal to zero as this is not allowed
    :param a: first user input
    """
    if a == 0:
        print("Zero Divisor Error - \u2018a\u2019 must not equal 0")
        quit()


def discriminant(a, b, c):
    """
    finds the discriminant given the variables a, b, and c
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :return d: the discriminant
    """
    check_a(a)
    try:
        d = float(b ** 2 - 4 * a * c)
        if d.is_integer():
            print("\nDiscriminant:", int(d))
        else:
            print("\nDiscriminant:", d)
        return d
    except OverflowError:
        print("OVERFLOW ERROR")
        quit()


def is_int(a, b, c):
    """
    checks to see if the float input is equal to an integer
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :return a, b, c: the inputs with possible changed types
    """
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)
    if c.is_integer():
        c = int(c)
    if a == 1:
        a = str(a).replace("1", "")
    if b == 1:
        b = str(b).replace("1", "")
    return a, b, c


def quadratic_roots(a, b, c, d):
    """
    solves for the quadratic formula
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :param d: the discriminant
    """
    a_print, b_print, c_print = is_int(a, b, c)
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
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        if root1.is_integer():
            root1 = int(root1)
        if root2.is_integer():
            root2 = int(root2)
        print("Two real roots found")
        print("x =", root1)
        print("x =", root2)
    elif d < 0:
        print("No real root(s) found")
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        print("Imaginary root found")
        root_i = str(root1)
        root_i = root_i.replace("(", "")
        root_i = root_i.replace("j", "𝑖")
        root_i = root_i.replace(")", "")
        root_i = root_i.replace("+", " \u00B1 ")
        print("x =", root_i)
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("One real root found")
        if root1.is_integer():
            root1 = int(root1)
        print("x =", root1)


def main():
    """
    runs program
    """
    a, b, c, = inputs()
    d = discriminant(a, b, c)
    quadratic_roots(a, b, c, d)


if __name__ == "__main__":
    main()
