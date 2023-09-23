nums = list(map(int, input().split())
count = nums[0]
nums.remove(nums[0])
for elem in range(1, count + 1):
    nums.append(elem)
res = 0
for num in nums:
    res ^= num
print(res)
