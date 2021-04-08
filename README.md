# The Chemyst library

To install chemyst run ```pip install chemyst```  

## Usage For P_total

```python
# PVnRT stands for Pressure, Volume, Number of Moles, R is the ideal gas law constant, T is temperature
from chemyst.PVnRT import P_total
# Mixture of 3 gases lets say
total_pressure = P_total([9.987, 2.33, 123.9])
print(total_pressure)
# OUTPUT: 136.217
```

Args:

- pressure is the only argument to P_total
  - It is a list of the partial pressure of all the gases in a mixture

## Usage For partial_pressure

```python
from chemyst.PVnRT import partial_pressure
# Args: num_moles, ideal_gas_law, temp, volume, is_temp_kelvin=True
pressureO2 = partial_pressure(2, 'atm', 31, 15.0, False)
print(pressureO2)
# OUTPUT: 13.2
```

Args:

- num_of_moles is the number of moles of the given gas  
- ideal_gas_law is the ideal gas law constant to use for the given pressure unit
  - if the pressure unit is atm
    - ideal_gas_law should be 'atm'
  - if the pressure unit is kpa
    - ideal_gas_law should be 'kpa'
  - if the pressure unit is mmHg
    - ideal_gas_law should be 'mmhg'
- temp is the given temperature can be either Celsius or Kelvin
- volume is the volume of the container
- is_temp_kelvin determines whether the temperature should be converter to Kelvin or not
  - if the temperature is in celsius is_temp_kelvin should equal false

## Usage For the moles_mass module

```python
from chemyst.moles_mass import moles_to_mass, mass_to_moles, atoms_to_grams, grams_to_atoms
# Moles to mass OUTPUT: 512g
moles_to_mass(16, 32)
# Mass to moles OUTPUT: 16.0
mass_to_moles(512, 32)
# Atoms to grams OUTPUT: 7.18e20
atoms_to_grams(1352, 32)
# Grams to atoms OUTPUT: 1.88e24 
grams_to_atoms(100, 32)
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

## Usage For the yields module

### Theoretical yield

The yields module is slightly different than the others  

the theoretical_yield() function takes 3 arguments:

- actual_yield
  - the yield given in the equation
- mole_ratio_top which is
  - From the balanced equation given, the number of moles of the wanted element
- mole_ratio_bottom which likewise is
  - From the balanced equation given, the number of moles of the given element

IMPORTANT: the theoretical_yield() function arguments MUST all be moles  
this can be easily achieved by using the ```moles_to_mass``` and ```mass_to_moles``` functions of ```chemyst.moles_mass```

### Percent Yield

the percent yield() function take 2 arguments

- actual_yield
  - yield given in the equation
- theoretical_yield
  - this yield can be calculated using the theoretical_yield() function

IMPORTANT: the percent_yield() function arguments MUST all be grams  
this can be easily achieved by using the ```moles_to_mass``` and ```mass_to_moles``` functions of ```chemyst.moles_mass```
