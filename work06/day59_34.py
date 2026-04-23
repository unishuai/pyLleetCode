# ============================================
# @File    : day59_34.py
# @Date    : 2026-04-20 23:09
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #也可以使用两次二分查找的方式
        l=0
        r=len(nums)-1

        idx=-1
        while l <=r:
            mid=(l+r)//2
            if nums[mid]==target:

                idx=mid
                break
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        if idx==-1:
            return [-1,-1]
        else:
            l=idx
            r=idx
            for i in range(idx,-1,-1):
                if nums[i]==target:
                    l=i
                else:
                    break

            for j in range(idx,len(nums)):
                if nums[j]==target:
                    r = j
                else:
                    break
            return [l,r]