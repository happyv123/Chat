cryptotext = open('cryptotext.txt','r')
nkey = open('n.txt', 'r')
dkey = open('d.txt', 'r')
text = open('text.txt', 'w')
c = int(cryptotext.read())
n = int(nkey.read())
d = int(dkey.read())
P = (c ** d) % n
text.write(str(P))