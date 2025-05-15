def ChkPrime(no):
    if no <= 1:
        return False
    
    if no == 2:
        return True
    
    if no % 2 == 0:
        return False
    
    for i in range(3, int(no ** 0.5) + 1, 2):
        if no % i == 0:
            return False
        
    return True
