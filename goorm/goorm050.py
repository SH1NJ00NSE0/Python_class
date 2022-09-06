n = int(input())
for i in range(1, n):
   print("*"*(i), end='')
   print(" "*(2*(n-i)), end='')
   print("*"*(i))
print("*"*(2*n))
for i in range(1, n):
   print("*"*(n-i), end='')
   print(" "*(2*i), end='')
   print("*"*(n-i))