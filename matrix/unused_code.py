#2304811 - 47 * int(2304811/47)
#2304811 - (47 * (2304811//47))
#(2304811/47 - 2304811//47) * 47

def remainder_without_mod (x, y):
    m = x - y * int(x/y)
    return m
