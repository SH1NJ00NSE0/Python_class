def print_arithmetic_operation(a,b):
   print(f"{a} + {b} = {a+b}")
   print(f"{a} - {b} = {a-b}")
   print(f"{a} * {b} = {a*b}")
   print(f"{a} / {b} = {a/b}")

a,b=input().split()
a=int(a)
b=int(b)
print_arithmetic_operation(a,b)