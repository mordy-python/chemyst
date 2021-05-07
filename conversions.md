# Conversions

## Moles and Mass conversion

```python
from chemyst.conversions import moles_to_mass, mass_to_moles
# Moles to mass OUTPUT: 512g
moles_to_mass(16, 32)
# Mass to moles OUTPUT: 16.0
mass_to_moles(512, 32)
```

The moles to mass and mass to moles functions both take 2 arguments

* The number of moles (for moles_to_mass)
* The grams of the element (for mass_to_moles)
* The second argument of both is the molar mass of the element

## Atoms and Grams conversion

```python
from chemyst.conversions import atoms_to_grams, grams_to_atoms
# Atoms to grams OUTPUT: 7.18e20
atoms_to_grams(1352, 32)
# Grams to atoms OUTPUT: 1.88e24
grams_to_atoms(100, 32)
```

The atoms to grams functions and grams to atoms functions take 2 arguments

* The number of atoms (for atoms_to_grams)
* The grams of the element (for grams_to_atoms)
* The second argument of both is the molar mass of the element

## Milliliters and Liters conversions

```python
from chemyst.conversions import ml_to_l, l_to_ml
# Mililiters to liters OUTPUT: 1 liter
ml_to_l(1000)
# Liters to mililiters OUTPUT: 1000ml
l_to_ml(1)
```

These two functions take 1 argument each

* To convert liters to milliliters, you pass in the number of liters to the l_to_ml function
* To convert milliliters to liters, you pass in the number of milliliters to the ml_to_l function