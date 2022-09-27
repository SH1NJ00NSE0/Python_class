import random
nums = random.sample(range(1,45),6) #행운 번호와 보너스 번호를 한번에
nums.sort()
luckNum=random.sample(range(1,45),1)
print(luckNum in nums)
if luckNum in nums:
	while luckNum not in nums:
		luckNum=random.sample(range(1,45),1)
print(f"행운번호 {nums} 보너스번호 {luckNum}")