import random
nums = random.sample(range(1,45),7) #행운 번호와 보너스 번호를 한번에
luckNum=nums.pop()
nums.sort()
print("행운 번호",nums,"보너스 번호",[luckNum])