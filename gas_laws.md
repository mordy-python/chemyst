# Gas Laws Module

## Usage For P_total

```python
# gas_laws stands for Pressure, Volume, Number of Moles, R is the ideal gas law constant, T is temperature
from chemyst.gas_laws import P_total
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
from chemyst.gas_laws import partial_pressure
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