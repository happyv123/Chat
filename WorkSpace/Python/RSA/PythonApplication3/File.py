global i, hislo

def prime(chislo):
    if chislo == 0 or chislo == 1:
        return True
    i = chislo -1
    while i>1:
        if (chislo % i) == 0:
            return True
        i -=1
    return False

def hislo(e):
    e+=2
    while prime(e):
        e += 2
    return e
l = 1
e = 1
while l<1000:
    print(str(hislo(e)))
    e = hislo(e)
    l+=1