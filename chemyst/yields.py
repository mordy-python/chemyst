def theoretical_yield(actual_yield, mole_ratio_top, mole_ratio_bottom):
    '''Finds theoretical_yield\n
    actual_yield:\n\tThe yield given in the equation if it is grams convert it to moles before using it \n
    mole_ratio_top:\n\tFrom the balanced equation given, the number of moles of the wanted element\n
    mole_ratio_bottom:\n\tFrom the balanced equation given, the number of moles of the given element'''
    yielded = actual_yield * (mole_ratio_top / mole_ratio_bottom)
    return yielded 

def percent_yield(actual_yield, theoretical_yield):
    '''Finds theoretical_yield\n
    actual_yield:\n\tThe yield given in the equation\n
    theoretical_yield:\n\tThis yield can be calculated with the theoretical_yield() function'''
    yielded = (actual_yield / theoretical_yield) * 100
    return yielded