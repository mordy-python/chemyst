def P_total(pressures=[]):
    '''Returns a float of the total pressure of a gas in a container
    \npressure: ```list``` \n\tList of pressures in a container'''
    total = 0.0
    for pressure in pressures:
        total += pressure
    return float(total)
