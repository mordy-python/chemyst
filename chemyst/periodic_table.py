# periodic table related functions

class InvalidAtomicNumber(Exception):
    """
    Error class for invalid atomic numbers.
    """
    pass

def _check_atomic_number(z:int) -> None:
    """
    Checks if the atomic number provided is valid or not.
    """
    if z <= 0:
        raise InvalidAtomicNumber("Atomic number (Z) of an element cant be zero or less than zero.")

    elif z > 118:
        raise InvalidAtomicNumber("Atomic number (Z) of an element cant be greater than 118.")


def electronic_config(z:int) -> str:
    """
    Returns the electronic configuration of an element corresponding to the Modern Periodic Table in string format.
    """
    _check_atomic_number(z)

    temp = z
    series = ['1S', '2S', '2P', '3S', '3P', '4S', '3D', '4P', '5S', '4D', '5P', '6S', '4F', '5D', '6P', '7S', '5F', '6D', '7P']

    result = ""

    for shell in series:
        if temp <= 0:
            break

        if shell.endswith("S"):
            if temp < 2:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}2 "
                temp -= 2

        elif shell.endswith("P"):
            if temp < 6:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}6 "
                temp -= 6

        elif shell.endswith("D"):
            if temp < 10:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}10 "
                temp -= 10

        elif shell.endswith("F"):
            if temp < 14:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}14 "
                temp -= 14

        else:
            print("Invalid subshell!")

    return result.rstrip()


def period_number(z:int) -> int :
    """
    Returns the period number of an element corresponding to the Modern Periodic Table.
    """
    _check_atomic_number(z)
    config = electronic_config(z).split(" ")
    ultimate_shell = 1
    for i in config:
        if int(i[0]) > ultimate_shell:
            ultimate_shell = int(i[0])

    return ultimate_shell
