class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        ls[0][0] = True

        
        for row in range(2, len(p) + 1):
            if p[row - 1] == "*":
                ls[row][0] = ls[row - 2][0]

        for row in range(1, len(p) + 1):
            for column in range(1, len(s) + 1):
                former_state = ls[row - 1][column - 1]
                current_regex = p[row - 1]
                if s[column - 1] == current_regex or current_regex == ".":
                    ls[row][column] = former_state
                elif p[row - 1] == "*":
                      
                      ls[row][column] = ls[row - 2][column]
                      if p[row - 2] == "." or p[row - 2] == s[column - 1]:
                          ls[row][column] |= ls[row][column -1]
        return ls[len(p)][len(s)]