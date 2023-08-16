class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: 
            return ""

        min_len = min(len(word) for word in strs)  
        output = ""

        for i in range(min_len):
            char = strs[0][i]  
            if all(word[i] == char for word in strs):
                output += char  
            else:
                break  

        return output