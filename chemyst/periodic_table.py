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
    # checking if the atomic number passed is valid
    _check_atomic_number(z)

    # a variable `temp` which will be decreased with number of electrons corresponding to
    # the subshell
    temp = z
    # all subshells in order
    series = ['1S', '2S', '2P', '3S', '3P', '4S', '3D', '4P', '5S', '4D', '5P', '6S', '4F', '5D', '6P', '7S', '5F', '6D', '7P']

    result = ""

    for shell in series:
        # breaking the loop if temp is 0, i.e., if the electronic configuration is complete
        if temp <= 0:
            break

        # S subshell can hold 2 electrons max, so deducting `temp` with 2 if it's greater
        # than 2 and substracting temp with itself if it's less than 2
        if shell.endswith("S"):
            if temp < 2:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}2 "
                temp -= 2

        # P subshell can hold 6 electrons max, so deducting `temp` with 6 if it's greater
        # than 6 and substracting temp with itself if it's less than 6
        elif shell.endswith("P"):
            if temp < 6:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}6 "
                temp -= 6

        # D subshell can hold 10 electrons max, so deducting `temp` with 10 if it's greater
        # than 10 and substracting temp with itself if it's less than 10
        elif shell.endswith("D"):
            if temp < 10:
                result += f"{shell}{temp} "
                temp -= temp
            else:
                result += f"{shell}10 "
                temp -= 10

        # P subshell can hold 14 electrons max, so deducting `temp` with 14 if it's greater
        # than 14 and substracting temp with itself if it's less than 14
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
    # checking if the atomic number passed is valid
    _check_atomic_number(z)

    # period number of an element is equal to the max subshell coefficient
    # so iterating through the config of the element to find the max one and returning 
    # the same
    config = electronic_config(z).split(" ")
    ultimate_shell = 1
    for i in config:
        if int(i[0]) > ultimate_shell:
            ultimate_shell = int(i[0])

    return ultimate_shell

# def group_number(z:int) -> int:
#     """
#     Returns the group number of an element corresponding to the Modern Periodic Table.
#     """
#     _check_atomic_number(z)

#     config = electronic_config(z).split(" ")

#     last_subshell_no = config[-1][0]
#     last_subshell = config[-1][1]
#     valence_electrons = 0

#     for i in config:
#         if last_subshell_no == i[0]:
#             valence_electrons += int(i[2:])

#     if last_subshell == "S":
#         return valence_electrons

#     elif last_subshell == "P":
#         return valence_electrons + 10

#     elif last_subshell == "D":
#         return "D block" 

#     elif last_subshell == "F":
#         return 3

#     else:
#         print("Invalid subshell")