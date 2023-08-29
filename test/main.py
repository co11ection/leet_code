matrix = [3, -7, 8, 6, 2]

def search(nums, target):
    
    for index in range(len(nums)):
        if nums[index] == target:
            return index
    return -1
    
print(search(matrix, target=8))
    
            
    
    

            

        