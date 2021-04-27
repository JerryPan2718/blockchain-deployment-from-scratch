class Solution:
    def rotation(self, matrix):
        self.counterClockwise(matrix)
        self.counterClockwise(matrix)
        self.counterClockwise(matrix)
        return matrix

    def counterClockwise(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            matrix[i] = matrix[i][::-1]

        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # return matrix


s = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.rotation(m))