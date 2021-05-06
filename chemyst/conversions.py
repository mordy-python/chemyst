def moles_to_mass(num_moles, molar_mass):  # Convert moles to mass
    grams = num_moles * molar_mass
    return grams


def mass_to_moles(g_of_element, molar_mass):  # Convert mass to moles
    moles = g_of_element / molar_mass
    return moles


def atoms_to_grams(num_atoms, molar_mass):  # Convert atoms to grams
    grams = (num_atoms / (6.02 * 10 ** 23)) * molar_mass
    return grams


def grams_to_atoms(g_of_element, molar_mass):  # Convert grams to atoms
    atoms = (g_of_element / molar_mass) * (6.02 * 10 ** 23)
    return atoms


def ml_to_l(ml):  # Convert milliliter to liter
    return ml * (1 / 1000)


def l_to_ml(l):  # Convert liter to milliliter
    return l * (1000 / 1)


def f_to_c(f):  # Convert fahrenheit to celsius
    return (f - 32) * 5 / 9


def f_to_k(f):  # Convert fahrenheit to kelvin
    return (f - 32) * 5 / 9 + 273.15


def c_to_f(c):  # Convert celsius to fahrenheit
    return (c * 9 / 5) + 32


def c_to_k(c):  # Convert celsius to kelvin
    return c + 273.15


def k_to_c(k):  # Convert kelvin to celsius
    return k - 273.15


def k_to_f(k):  # Convert kelvin to fahrenheit
    return (k - 273.15) * 9 / 5 + 32
