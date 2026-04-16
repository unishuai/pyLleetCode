# ============================================
# @File    : day13_238.py
# @Date    : 2026-04-02 9:35
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nLen=len(nums)
        dpL=[0]*nLen
        dpL[0]=nums[0]
        dpR=[0]*nLen

        for i in range(1,nLen):
            dpL[i]=dpL[i-1]*nums[i]

        dpR[-1] = nums[-1]
        for i in range(nLen-2,-1,-1):
            dpR[i]=dpR[i+1]*nums[i]

        res=[0]*nLen
        res[0]=dpR[1]
        res[-1]=dpL[-2]
        for i in range(1,nLen-1):
            res[i]=dpL[i-1]*dpR[i+1]
        return res




t=Solution()
print(t.productExceptSelf(nums=[1, 2, 3, 4]))