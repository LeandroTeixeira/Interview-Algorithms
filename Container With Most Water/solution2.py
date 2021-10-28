def maxArea(height,verbose = False,technique = 0) -> int:
    if technique == 0:
        return divide_and_conquer(height,verbose)["area"]
    else:
        i, j = 0, len(height) - 1
        area = min (height[i],height[j]) * (j-i)
        i_a, j_a = i,j
        while i < j:
            if height[i] < height[j]:
                while height[i] < height[j] and i < len(height):
                    i +=1
                    if (min (height[i],height[j]) * (j-i) > area):
                        area = min (height[i],height[j]) * (j-i)
                        i_a,j_a = i,j
                    
            else:
                while height[j] <= height[i] and j >= 0:
                    j -= 1
                    if min (height[i],height[j]) * (j-i) > area:
                        area = min (height[i],height[j]) * (j-i)
                        i_a,j_a = i,j
                         
        return [i_a,j_a, area]