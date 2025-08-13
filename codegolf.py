import sys
l = 'IVXLCDM '
for n in [int(x) for x in open(sys.argv[1],"r").readlines()]:
	f = ''
	for i in [3,2,1,0]:
		x = l[i*2]
		v = int(n/10**i)%10
		f += f'{x}{l[i*2+int(v/5)+1]}' if v%5==4 else l[i*2+1]*int(v/5)+x*(v%5)
	print(f)