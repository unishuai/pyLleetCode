# ============================================
# @File    : day17_240.py
# @Date    : 2026-04-10 10:42
# @Author  : 帅宇昕
# ============================================
import bisect
from typing import List





class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     mlen=min(len(matrix),len(matrix[0]))
    #     if target<matrix[0][0] or target>matrix[-1][-1]:
    #         return False
    #     # left=0
    #     # right=mlen-1
    #     # while left<right:
    #     #     if matrix[left][left]==target or matrix[right][right]==target:
    #     #         return True
    #     #     if matrix[left][left] <target:
    #     #         left+=1
    #     #     if left==right:
    #     #         break
    #     #     if matrix[right][right]:
    #     #         left+=1
    #
    #     # for i in range(mlen):
    #     #     if matrix[i][i] > target:
    #     #         for j in range(i):
    #     #             if matrix[i][j]==target or matrix[j][i]==target:
    #     #                 return True
    #     #
    #     #         return False
    #     #     elif matrix[i][i] == target:
    #     #         return True
    #     # if len(matrix[0]) > len(matrix):
    #     #     #列大
    #     # return False
    #     #这个是二分查找
    #     for row in matrix:
    #         idx=bisect.bisect_left(row,target)
    #         if idx < len(row) and row[idx] == target:
    #             return True
    #         return False


    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     #从左往右，从上往下都是变大的，可以把它看成一个树
    #     #树的根节点是matrix[0][-1]
    #     if target < matrix[0][0] or target > matrix[-1][-1]:
    #         return False
    #
    #     left=0
    #     right=len(matrix[0])-1
    #     root=matrix[left][right]
    #     nlen=len(matrix)
    #     while right>=0 and left<nlen:
    #         if target == matrix[left][right]:
    #             return True
    #         elif target < matrix[left][right]:
    #             right-=1
    #         else :
    #             left+=1
    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rlen = len(matrix[0])
        for row in matrix:
            index=self.getIndex(row,target)
            if index !=  rlen:
                return True
        return False


    def getIndex(self,row, target):
        rlen=len(row)
        left=0
        right=rlen-1
        while left<=right:
            media=(right+left)//2
            if target==row[media]:
                return media
            elif target>row[media]:
                left=media+1
            else:
                right=media-1
        return  rlen






