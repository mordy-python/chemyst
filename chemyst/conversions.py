#  Mass conversions
def moles_to_mass(num_moles, molar_mass):  # Convert moles to mass
    grams = num_moles * molar_mass
    return grams


def mass_to_moles(g_of_element, molar_mass):  # Convert mass of an element to moles
    moles = g_of_element / molar_mass
    return moles


def atoms_to_grams(num_atoms, molar_mass):  # Convert atoms to grams
    grams = (num_atoms / (6.02 * 10 ** 23)) * molar_mass
    return grams


def grams_to_atoms(g_of_element, molar_mass):  # Convert element grams to atoms
    atoms = (g_of_element / molar_mass) * (6.02 * 10 ** 23)
    return atoms


def grams_to_milligrams(gram):  # Convert grams to milligrams
    return gram * 1000


def grams_to_kilograms(gram):  # Convert grams to kilograms
    return gram / 1000


def milligrams_to_grams(milligram):  # Convert milligrams to grams
    return milligram / 1000


def milligrams_to_kilograms(milligram):  # Convert milligrams to kilograms
    return milligram / 1e+6


def kilograms_to_grams(kilogram):  # Convert kilograms to grams
    return kilogram * 1000


def kilograms_to_milligrams(kilogram):  # Convert kilograms to milligrams
    return kilogram * 1e+6


def pounds_to_tons(p):  # Convert pounds to tons
    return p / 2000


def tons_to_pounds(t):  # Convert tons to pounds
    return t * 2000


# Volume conversions (US unit conversions, not Imperial units)
def ml_to_l(ml):  # Convert milliliter to liter
    return ml * (1 / 1000)


def l_to_ml(l):  # Convert liter to milliliter
    return l * (1000 / 1)


def gallon_to_quart(gallon):  # Convert gallons to quarts
    return gallon * 4


def gallon_to_pint(gallon):  # Convert gallons to pints
    return gallon * 8


def gallon_to_ounce(gallon):  # Convert gallons to ounces
    return gallon * 128


def quart_to_gallon(quart):  # Convert quarts to gallons
    return quart / 4


def quart_to_pint(quart):  # Convert quarts to pints
    return quart * 2


def quart_to_ounce(quart):  # Convert quarts to ounces
    return quart * 32


def pint_to_gallon(pint):  # Convert pints to gallons
    return pint / 8


def pint_to_quart(pint):  # Convert pints to quarts
    return pint / 2


def pint_to_ounce(pint):  # Convert pints to ounces
    return pint * 16


def ounce_to_quart(ounce):  # Convert ounces to quarts
    return ounce / 32


def ounce_to_gallon(ounce):  # Convert ounces to gallons
    return ounce / 128


def ounce_to_pint(ounce):  # Convert ounces to pints
    return ounce / 16


# Length conversions
def foot_to_inch(foot):  # Convert feet to inches
    return foot * 12


def foot_to_mile(foot):  # Convert feet to miles
    return foot / 5280


def foot_to_yard(foot):  # Convert feet to yard
    return foot / 3


def inch_to_foot(inch):  # Convert inches to feet
    return inch / 12


def inch_to_yard(inch):  # Convert inches to yards
    return inch / 36


def inch_to_mile(inch):  # Convert inches to miles
    return inch / 63360


def yard_to_foot(yard):  # Convert yard to feet
    return yard * 3


def yard_to_inch(yard):  # Convert yards to inches
    return yard * 36


def yard_to_mile(yard):  # Convert yards to miles
    return yard / 1760


def mile_to_foot(mile):  # Convert miles to feet
    return mile * 5280


def mile_to_inch(mile):  # Convert miles to inches
    return mile * 63360


def mile_to_yard(mile):  # Convert miles to yards
    return mile * 1760


#  Temperature conversations
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
