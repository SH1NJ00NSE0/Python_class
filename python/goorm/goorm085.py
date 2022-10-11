class Unit:
   def __init__(self, name, hp,damage):
      self.name = name
      self.hp = hp
      self.damage=damage
      print("{} 유닛이 생성되었습니다.".format(self.name))
      print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
 
def attack(name,location,damage):
   print("\n{0} : {1} 방량으로 적군을 공격합니다. 공격력 {2}"
         .format(name,location,damage))

marine1=Unit("마린",40,5)
marine2=Unit("마린",40,5)
tank=Unit("탱크",150,35)

attack(marine1.name,"1시",marine1.damage)
attack(marine2.name,"1시",marine2.damage)
attack(tank.name,"1시",tank.damage)

print()