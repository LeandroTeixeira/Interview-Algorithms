def longestPalindrome(s: str) -> str:
    if (len (s) == 0):
        return ""
    
    # The base scenario is a string with the biggest palyndrome being of size one
    # So, we start with this scenario in mind and choose the first character
    longest = s[0]
    
    # The idea here is pretty simple: we iterate through the string. For every character, we build the biggest palyndrome
    # possible with that character as the central character of the palnydrome. If two identical characters are next to each
    # other, we also test the scenario that the biggest palyndrome has an even size and they are the central part
    
    
    for i in range(1,len(s)):
        long = s[i]
        j = i-1
        k = i+1
        
        # To find the biggest possible palyndrome from a certain point, we compare the closest character to the left and to the
        # right and if they are, we compare the next chracters until we find a different pair or reach the end of the string
        while j>=0 and k < len(s) and s[j] == s[k]:
            long = s[j]+long+s[k]
            j -= 1
            k += 1
        # We then compare the size of the biggest palyndrome found. If it's bigger than the highest so far, it becomes the
        # new biggest
        if len(long) > len(longest):
            longest = long
    
        # We also test for the scenario where the palyndrome has an even size. For it to happen, the middle part of the 
        # Palyndrome must have the same character twice in a row
        if (s[i] == s[i-1]):
            k = i
            j = i-1
            long = ""
            while j>=0 and k < len(s) and s[j] == s[k]:
                long = s[j]+long+s[k]
                j -= 1
                k += 1
            if len(long) > len(longest):
                    longest = long
        
        
    return longest