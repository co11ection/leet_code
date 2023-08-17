class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
        if not digits:
            return []
        result = []
    
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
        
            digit = digits[index]
            possible_letters = letters[digit]
        
            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)
        backtrack(0, "")
        return result