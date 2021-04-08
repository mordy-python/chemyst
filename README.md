# The Chemyst library

Note: As of now this library is in development

To install chemyst run ```pip install chemyst```  
Currently there are two functions available  

- ```P_total()```
- ```partial_pressure()```

Function #1 finds the total pressure of a mixture of gases
Function #2 finds the partial pressure of a single gas in a mixture of gases

## Usage For P_total

```python
# PVnRT stands for Pressure, Volume, Number of Moles, R is the ideal gas law constant, T is temperature
from chemyst.PVnRT import P_total
# Mixture of 3 gases lets say
total_pressure = P_total([9.987, 2.33, 123.9])
print(total_pressure)
# OUTPUT: 136.217
```

## Usage For partial_pressure

```python
from chemyst.PVnRT import partial_pressure
# Args: num_moles, ideal_gas_law, temp, volume, is_temp_kelvin=True
pressureO2 = partial_pressure(2, 'atm', 31, 15.0, False)
print(pressureO2)
# OUTPUT: 13.2
```
