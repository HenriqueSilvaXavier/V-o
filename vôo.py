import random
A=[".", ".", ".", ".", ".", "."]
c=random.randint(0,len(A)-1)
A[c]="🐦"
A2=""
for n in A:
	A2=A2+n
print(A2)
for n in range(0,7):
	A=[".", ".", ".", ".", ".", "."]
	if c>0 and c<len(A)-1:
		lista=[c-1, c+1]
	elif c==0:
		lista=[c+1]
	elif c==len(A)-1:
		lista=[c-1]
	c=random.choice(lista)
	A[c]="🐦"
	A2=""
	for n in A:
		A2=A2+n
	print(A2)