class human:
   def __init__(self,height,age):
      self.height=height
      self.age=age
   
   def how_old(self):
      print(self.age,"살 입니다.")
      
   def how_tall(self):
      print(self.height,"cm 입니다.")

Seunghyun=human(180,31)
Seunghyun1=human(180,31)
Seunghyun2=human(180,31)

print(Seunghyun1 == Seunghyun2)
Seunghyun.weight=90