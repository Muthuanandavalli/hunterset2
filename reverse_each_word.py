S=input()
N=len(S)
S1,S2=S.split()
for x in range(len(S1)-1,-1,-1):
	print(S1[x],end="")
print(" ",end="")
for y in range(len(S2)-1,-1,-1):
	print(S2[y],end="")
 
