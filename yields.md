# Yields

## Usage

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
this can be easily achieved by using the ```moles_to_mass``` and ```mass_to_moles``` functions of ```chemyst.conversions```

### Percent Yield

the percent yield() function take 2 arguments

- actual_yield
  - yield given in the equation
- theoretical_yield
  - this yield can be calculated using the theoretical_yield() function

IMPORTANT: the percent_yield() function arguments MUST all be grams  
this can be easily achieved by using the ```moles_to_mass``` and ```mass_to_moles``` functions of ```chemyst.conversions```