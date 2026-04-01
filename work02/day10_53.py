# ============================================
# @File    : day10_53.py
# @Date    : 2026-04-01 17:05
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nLen=len(nums)
        if nLen==1:
            return nums[0]
        dp=[0]*nLen
        dp[0]=nums[0]

        nmax=nums[0]
        for i in range(1,nLen):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
            nmax=max(nmax,dp[i])
        return nmax





t=Solution()
print(t.maxSubArray([5,4,-1,7,8]))