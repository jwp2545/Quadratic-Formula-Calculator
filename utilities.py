def check_a(a):
    # Checks if parameter is equal to 0 in order to prevent Zero Division Error
    if a == 0:
        print("Zero Divisor Error - \u2018a\u2019 must not equal 0")
        quit()


def is_int(a, b, c):
    """
    checks to see if the float input is equal to an integer
    :param a: first user input
    :param b: second user input
    :param c: third user input
    :return a, b, c: the inputs with possible changed types
    """
    # Checks if parameters are integers and if so changes them to int type
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)
    if c.is_integer():
        c = int(c)
    if a == 1:
        # If coefficient is equal to 1, replace with empty string
        a = str(a).replace("1", "")
    if b == 1:
        b = str(b).replace("1", "")
    return a, b, c
