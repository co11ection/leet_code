s = 'TIMATITIMA'
numRows = 3
result = ''
first_row = max(1, 2 * (numRows - 1))

for i in range(numRows):
    for pos, symb in enumerate(s):
        if (pos + i) % first_row == 0 or (pos - i) % first_row == 0:
            result = result + symb
print(result)