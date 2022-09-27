import random
nums = random.sample(range(1,45),6) #행운 번호와 보너스 번호를 한번에
nums.sort()
luckNum=random.randint(1,45)
while luckNum in nums:
	luckNum=random.randint(1,45)
print(f"행운번호 {nums} 보너스번호[{luckNum}]")