import math

def solution (test):
    '''
    Description:
        This function iterates through the array comparing the current value with the lowest found so far and see if it makes a profit higher than the best one found so far. Infinity and minus infinity are used as the starting lowest price and max profit, respectively\n
        Note that the highest profit returned can be negative if the price goes only down\n
    Complexity: O(n)
        We iterate through the array only once
    '''
    lowest_price = math.inf
    max_profit = -math.inf
    for i in test:
        if (n:= i - lowest_price) > max_profit:
            max_profit = n
        if i < lowest_price:
            lowest_price = i 
    return max_profit 

