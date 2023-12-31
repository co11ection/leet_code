class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if not s:
            return 0
        sign =  1
        if s[0]  in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
    
        result = 0
        for element in s:
            if element.isdigit():
                result =  result * 10 + int(element)
            else:
                break
        result *= sign


        return max(min(result, INT_MAX), INT_MIN)
            

        