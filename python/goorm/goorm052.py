import random
nums = []

while len(nums) < 6:
   num = random.randint(1, 45)
   if num not in nums:
      nums.append(num)
nums.sort()
print(nums)
