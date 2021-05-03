
def P_total(pressures=[]):
    '''Returns a float of the total pressure of a gas in a container
    \npressure: ```list``` \n\tList of pressures in a container'''
    total = 0.0
    for pressure in pressures:
        total += pressure
    return float(total)


def partial_pressure(num_moles, ideal_gas_law, temp, volume, is_temp_kelvin=True):
    '''Returns the partial pressure of a given gas in a mixture\n
    num_moles:\n\tNumber of moles of the gas in the reaction\n
    ideal_gas_law:\n\tMust be any of the following: kpa, atm, or mmhg\n
    temp:\n\tTemperature of the gas\n\t\tMust be either Kelvin or Celsius\n
    volume:\n\tVolume of the container in liters\n
    is_temp_kelvin:\n\tIf the temperature is Celsius this should be set to false otherwise leave it'''
    ATM = 0.0821
    KPA = 8.314
    MMHG = 62.4
    if ideal_gas_law == 'atm':
        ideal_gas_law_number = ATM
    if ideal_gas_law == 'kpa':
        ideal_gas_law_number = KPA
    if ideal_gas_law == 'mmhg':
        ideal_gas_law_number = MMHG
    if not is_temp_kelvin:
        temp += 273
    nrt = (num_moles) * (ideal_gas_law_number) * (temp)
    final_pressure = nrt/volume
    return final_pressure
