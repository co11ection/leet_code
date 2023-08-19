class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        answer = []
        while matrix:
            answer += matrix[0]
            matrix.pop(0)
        
            if matrix:
                for element in matrix:
                    if element:
                        answer.append(element.pop())
        
            if matrix and matrix[-1]:
                answer += matrix[-1][::-1]
                matrix.pop()
            
            if matrix:
                for element in matrix[::-1]:
                    if element:
                        answer.append(element.pop(0))

        return answer