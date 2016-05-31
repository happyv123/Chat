cryptotext = open('cryptotext.txt','w')
ekey = open('e.txt', 'r')
nkey = open('n.txt', 'r')
P = int( input("Enter your msg: ") ) 
e = int( ekey.read() )
n = int( nkey.read() )
c = P ** e % n
cryptotext.write(str(c))