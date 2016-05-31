fi=open('input.txt','r')
fo=open('output.txt','w')
a=int(fi.read())
s=(1+a)*abs(a)/2
fo.write(str(int(s)))
fo.close()
fi.close()
