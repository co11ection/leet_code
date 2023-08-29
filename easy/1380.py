class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
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