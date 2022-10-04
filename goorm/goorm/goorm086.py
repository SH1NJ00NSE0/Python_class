class Unit:
   def __init__(self,name,hp):
      self.name=name
      self.hp=hp
   
class AttackUnit:
   def __init__(self, name, hp,damage):
      self.name = name
      self.hp = hp
      self.damage=damage
      # print("{} 유닛이 생성되었습니다.".format(self.name))
      # print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
 
   def attack(self,location):
      print("\n{0} : {1} 방량으로 적군을 공격합니다. [공격력 {2}]"
            .format(self.name,location,self.damage))

   def damaged(self,damage):
      print("{0} : {1} 데미지를 입었습니다."
            .format(self.name, damage))

      self.hp-=damage
      print("{0} : 현재 체력은 {1}입니다."
            .format(self.name,self.hp))
      
      if self.hp<=0:
         print("{0} : 파괴되었습니다."
               .format(self.name))

class Flyable:
   def __init__(self,flying_speed):
      self.flying_speed = flying_speed
   
   def fly(self,name,location):
      print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
            .format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
   def __init__(self, name, hp, damage,flying_speed):
      AttackUnit.__init__(self,name,hp,damage)
      Flyable.__init__(self,flying_speed)

valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")

firebat1=AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)
# tank=Unit("탱크",150,35)

# attack(marine1.name,"1시",marine1.damage)
# attack(marine2.name,"1시",marine2.damage)
# attack(tank.name,"1시",tank.damage)

# wrait1=Unit("레이스",80,5)
# print("유닛이름 : {0}, 공격력 : {1}\n"
#       .format(wrait1.name,wrait1.damage))

# wrait2=Unit("빼앗은 레이스",80,5)
# wrait2.clocking=True

# if wrait2.clocking==True:
#    print("{0}는 현재 클로킹 상태입니다.".format(wrait2.name))

print()