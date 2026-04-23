# ============================================
# @File    : day57_35.py
# @Date    : 2026-04-20 21:53
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]== target:
                return mid
            elif nums[mid]>target:
                r = mid - 1

            else:
                l = mid + 1


        return max(l,r)

