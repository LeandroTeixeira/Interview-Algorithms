def brute_force(height):
    max_area = 0
    for i,v1 in enumerate(height):
        for j,v2 in enumerate(height):
            if j <= i:
                continue
            if min(v1,v2) * (j-i) > max_area:
                max_area = min(v1,v2) * (j-i)
    return max_area