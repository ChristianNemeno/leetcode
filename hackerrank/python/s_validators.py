if __name__ == '__main__':
    s = input()
    
    hasalnum = False
    hasalpha = False
    hasdigit = False
    haslower =False
    hasupper = False
    
    for c in s:
        if c.isalnum():
            hasalnum = True
        if c.isalpha():
            hasalpha = True
        if c.isdigit():
            hasdigit = True
        if c.islower():
            haslower = True
        if c.isupper():
            hasupper = True
            
    print(hasalnum)
    print(hasalpha)
    print(hasdigit)
    print(haslower)
    print(hasupper)
        
