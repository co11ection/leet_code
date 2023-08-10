class Solution:
    def reverse(self, x: int):
        try:
            x = int(str(x)[::-1])
        except ValueError:
            x = int('-'+str(x)[::-1][:-1])
        finally:
            if abs(x) > 2**31:
                return 0
            return x