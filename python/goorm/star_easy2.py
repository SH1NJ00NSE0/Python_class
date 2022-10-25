n=int(input())
for x in range(n+1):
	print(" " * (n-x),end="")
	print("*" * x)