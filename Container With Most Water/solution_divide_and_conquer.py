def divide_and_conquer (height,verbose = False):
    if (len(height) > 1):
        left = divide_and_conquer(height[0:(math.floor(len(height)/2))],verbose)
        right = divide_and_conquer (height[(math.floor(len(height)/2)):],verbose)
    if (len(height) == 1):
        answer = {
            "array":height,
            "left":[height[0],0],
            "right":[height[0],0],
            "area":0
        }
    else:
        l_len = len (left["array"])
        r_len = len (right["array"])
        right["left"][1] += l_len
        right["right"][1] += l_len
        array = left["array"] + right ["array"]
        
        if  (left["left"][0]*(l_len - left["left"][1]) < left ["right"][0]*(l_len - left["right"][1])):
            l = left["right"][1]
        else:
            l = left["left"][1]
                
        if  (right["right"][0]* right["right"][1] < right ["left"][0]* right["left"][1]):
            r = right["left"][1]
        else:
            r = right["right"][1]
        
        dist = r - l
        area = min (array[l] * dist, array[r] * dist)
        
        if left["area"] >= area and left ["area"] >= right["area"]:
            answers = [left["left"],left["right"],left["area"]]
        elif right["area"] >= area and right ["area"] >= right["area"]:
            answers = [right["left"],right["right"],right["area"]]
        else:      
            answers = [[array[l],l],[array[r],r], area]
        
                    
        answer = {
            "array": array,
            "left": answers[0],
            "right": answers[1],
            "area": answers[2]
        }
        
        if(verbose):
            print (f'{answer["array"]}: {answer["left"]} / {answer["right"]} = {answer["area"]} ')
    return answer
        
def maxArea(height,verbose = False) -> int:
    return divide_and_conquer(height,verbose)["area"]
    
    