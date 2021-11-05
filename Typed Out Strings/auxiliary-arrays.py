def clean_string (s):
    c_str = []
    for c in s:
        if c == "#":
            if len(c_str) > 0:
                c_str.pop()
        else:
            c_str.append(c)
    return c_str

def typed_out_strings (s,t, technique):
    if (technique < 0):
        return clean_string(s) == clean_string(t)   