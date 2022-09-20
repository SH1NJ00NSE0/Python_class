def cal(a,b,op):
   if op=='+': return a+b
   if op=='-': return a-b
   if op=='x': return a*b
   if op=='/': return a/b

a,op,b=input().split()
a=int(a)
b=int(b)
print(f"{a} {op} {b} = {cal(a,b,op)}")