# Conversions

## Usage

```python
from chemyst.conversions import moles_to_mass, mass_to_moles, atoms_to_grams, grams_to_atoms, ml_to_l, l_to_ml
# Moles to mass OUTPUT: 512g
moles_to_mass(16, 32)
# Mass to moles OUTPUT: 16.0
mass_to_moles(512, 32)
# Atoms to grams OUTPUT: 7.18e20
atoms_to_grams(1352, 32)
# Grams to atoms OUTPUT: 1.88e24 
grams_to_atoms(100, 32)
# Mililiters to liters OUTPUT: 1 liter
ml_to_l(1000)
# Liters to mililiters OUTPUT: 1000ml
l_to_ml(1)
```

Args:

- moles_to_mass(num_moles, molar_mass)
  - num_moles is the number of moles to be converted to grams
  - molar_mass is the mass of the element in grams
    - for example O2 would have a molar mass of 32
- mass_to_moles(g_of_element, molar_mass)
  - g_of_element is the amount of grams which will be converted to moles
  - molar_mass is the mass of the element in grams
- atoms_to_grams(num_atoms, molar_mass)
  - num_atoms is the number of atoms to be converted to grams
  - molar_mass is the mass of the element in grams
- grams_to_atoms(g_of_element, molar_mass)
  - g_of_element is the amount of grams which will be converted to moles
  - molar_mass is the mass of the element in grams
- ml_to_l(ml)
  - ml is the number of mililiters to convert into liters
- l_to_ml(l)
  - l is the number of liters to convert into mililiters