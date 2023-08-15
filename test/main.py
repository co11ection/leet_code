numRows = 4
s = 'HELLOWORLD'
result = ""
first_row = max(1, 2 * (numRows - 1))
for i in range(numRows):
    for ind, element in enumerate(s):
        if (ind + i) % first_row == 0 or (ind - i) % first_row == 0:
            result += element
print(result)
