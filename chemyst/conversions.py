def moles_to_mass(num_moles, molar_mass):
    grams = num_moles * molar_mass
    return grams


def mass_to_moles(g_of_element, molar_mass):
    moles = g_of_element / molar_mass
    return moles


def atoms_to_grams(num_atoms, molar_mass):
    grams = (num_atoms / (6.02*10**23)) * molar_mass
    return grams


def grams_to_atoms(g_of_element, molar_mass):
    atoms = (g_of_element / molar_mass) * (6.02*10**23)
    return atoms


def ml_to_l(ml):
    return ml*(1/1000)


def l_to_ml(l):
    return l*(1000/1)
