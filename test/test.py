num = 10342
rom_number = {
            1: "I", 
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "IL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM"
        }
result = ""
ls = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

print(ls)
for n in ls:
    while n<=num:
        result += rom_number[n]
        num -= n
print(result)