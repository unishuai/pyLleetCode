# ============================================
# @File    : day58_74.py
# @Date    : 2026-04-20 22:29
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        rline=len(matrix[0])-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][rline]==target:
                return True
            elif matrix[mid][rline]>target:
                r=mid-1
            else:
                l=mid+1
        inRow=max(r,l)
        if inRow>=len(matrix):
            return False
        l = 0
        r=rline
        while l<=r:
            mid=(l+r)//2
            if matrix[inRow][mid]==target:
                return True
            elif matrix[inRow][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
