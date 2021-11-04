# This goes with the two pointer technique, using the fact that the area scales with the lower of the two values and the distance between them
# We initialize two pointers at the opposite sides of the array (maximizing distance). Then we take the lesser of the two values and iterate the pointer
# until a higher value is found, then the area is calculated and compared to the best one registered so far.

# We repeat this process until either the pointers cross each other or they reach the end of the array

def maxArea(height) -> int:
    i, j = 0, len(height) - 1
    area = min (height[i],height[j]) * (j-i)
    # While not required, here we also use two variables to save the indices that together make the biggest area
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
                         
    return area