

def strcount(s):
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) + 1
    
    for key, value in dct.items():
        print(key, value)

strcount('aaabcd')