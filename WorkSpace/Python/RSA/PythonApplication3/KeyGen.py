import random
ekey = open('e.txt', 'w')
nkey = open('n.txt', 'w')
dkey = open('d.txt', 'w')
global i, randomchislo


def prime(chislo):
    if chislo == 0 or chislo == 1:
        return True
    i = chislo -1
    while i>1:
        if (chislo % i) == 0:
            return True
        i -=1
    return False


def randomprime(maxint):
    randomchislo = random.randint(500, maxint)
    while prime(randomchislo):
        randomchislo = random.randint(500, maxint)
    return randomchislo

def hislo(e):
    e+=2
    while prime(e):
        e += 2
    return e

p = randomprime(1000)
q = randomprime(1000)


n = p * q


phi = (p-1)*(q-1)

r = phi / 3
e = 1
e  = hislo(e)

while (phi % e) == 0:
    e = hislo(e)

i = 1
d = (phi * i + 1) / e
i += 1
while d % 1 != 0:
    d = (phi * i + 1) / e
    i+=1


ekey.write( str(e) )
dkey.write( str( int(d) ) )
nkey.write( str(n) )