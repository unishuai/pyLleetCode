# ============================================
# @File    : day15_54.py
# @Date    : 2026-04-08 21:09
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     row=len(matrix)
    #     line=len(matrix[0])
    #     cRow=row
    #     cline=line
    #     res=[]
    #     m=0
    #     n=0
    #     while True:
    #         for i in range(cline):
    #            tmp= matrix[m][n]
    #            res.append(tmp)
    #            n+=1
    #         n-=1
    #         m+=1
    #         cRow-=1
    #         if cline<=0 or cRow<=0 or  (cline==0 and cRow==0):
    #             break
    #
    #
    #         for j in range(cRow):
    #             tmp = matrix[m][n]
    #             res.append(tmp)
    #             m += 1
    #         m-=1
    #         n-=1
    #         cline-=1
    #         if cline<=0 or cRow<=0 or  (cline==0 and cRow==0):
    #             break
    #
    #         for i in range(cline):
    #            tmp= matrix[m][n]
    #            res.append(tmp)
    #            n-=1
    #         n += 1
    #         m -= 1
    #         cRow-=1
    #         if cline<=0 or cRow<=0 or  (cline==0 and cRow==0):
    #             break
    #
    #         for j in range(cRow):
    #             tmp = matrix[m][n]
    #             res.append(tmp)
    #             m -= 1
    #         m += 1
    #         n += 1
    #         cline -= 1
    #         if cline<=0 or cRow<=0 or  (cline==0 and cRow==0):
    #             break
    #     return  res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order




t=Solution()
print(t.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))