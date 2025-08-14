import sys
l = 'IVXLCDM '
for p in open(sys.argv[1],"r"):
	f=''
	for i in [6,4,2,0]:
		v=int(p)//10**(i//2)%10
		f+=l[i]+l[i+v//5+1] if v%5==4 else v//5*l[i+1]+v%5*l[i]
	print(f)