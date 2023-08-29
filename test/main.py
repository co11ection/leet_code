matrix = [[3,7,8],[9,11,13],[15,16,17]]

def luckyNumber(matrix):
    row, columb = len(matrix), len(matrix[0])
    s = set()
    lucky_nums = []
    for index_i in range(row):
        s.add(min(matrix[index_i]))
    for element in zip(*matrix):
        t = max(element)
        if t in s:
            lucky_nums.append(t)
    return lucky_nums
        
    
    

            

        