nums = [1, 2, 3, 1, 5, 4, 2]
hashmap = {i: 0 for i in nums}

n = len(nums)
for i in range(n):
    if hashmap[nums[i]] == 0:
        print(nums[i], end=" ")
        hashmap[nums[i]] = 1
