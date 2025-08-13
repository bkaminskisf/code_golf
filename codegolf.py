import sys
def main():
	if len(sys.argv) < 1:
		sys.exit(1)
	with open(sys.argv[1], "r") as g:
		e = [int(x) for x in g.readlines()]
	l = 'IVXLCDM  '
	for n in e:
		f = ''
		for i in [3,2,1,0]:
			x = l[i*2]
			v = int(n/10**i) % 10
			if v % 5 == 4:
				f += f'{x}{l[i*2+int(v/5)+1]}'
			else:
				f += l[i*2+1]*int(v/5)
				f += x*(v % 5)
		print(f)
if __name__ == "__main__":
	main()