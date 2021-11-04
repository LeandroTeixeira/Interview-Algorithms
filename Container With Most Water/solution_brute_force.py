
# This is the brute force solution. We check all possible areas (with a little adjustment to not count the same area twice)
# Since we need to iterate the array once for each element, this solution runs in O (n²)
def brute_force(height):
    max_area = 0
    for i,v1 in enumerate(height):
        for j,v2 in enumerate(height):
            if j <= i:
                continue
            if min(v1,v2) * (j-i) > max_area:
                max_area = min(v1,v2) * (j-i)
    return max_area