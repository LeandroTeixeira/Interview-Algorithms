def solution(list):
    '''
    Description:
        The solution can be broken down into smaller steps. For each number, we are multiplying the product of the numbers before it by the multiplication of those after it. By calculating these values, we can pass through the array only twice to arrive at the solution.\n
    Complexity: O(n). We only iterate through the array twice
    '''
    aux = [None]*len(list)
    resul = [None]*len(list)
    current_mul = 1
    
    for i in range(len(list)-1,-1,-1):
        aux[i] = current_mul
        current_mul *= list[i]

    current_mul = 1
    for i in range (0,len(list)):
        resul[i] = aux[i] * current_mul
        current_mul *= list[i]

    return resul