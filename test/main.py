nums = [1, 2, 4]
target = 5
index = 0
for ind, num in enumerate(nums):
    if num < target:
        if nums[-1] < target:
            index = ind + 1
        else: 
            index = ind
            continue
    elif num == target:
        index = ind
    elif num > target:
        index = ind

print(index)