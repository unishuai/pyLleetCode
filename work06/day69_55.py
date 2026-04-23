# ============================================
# @File    : day69_55.py
# @Date    : 2026-04-23 10:41
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # 输入：nums = [2, 3, 1, 1, 4]
    # 输出：true
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums)<=1:
    #         return True
    #     #这个跳跃游戏不经让我想起了爬楼梯
    #     dp=[0]*len(nums)
    #     dp[-1]=1
    #     for i in range(len(nums)-2,-1,-1):
    #         k=nums[i]+i+1
    #         if k>len(nums):
    #             k=len(nums)
    #         for j in range(i+1,k):
    #             if dp[j]==1:
    #                 dp[i]=1
    #                 break
    #     return bool(dp[0])

    def canJump(self, nums: List[int]) -> bool:
        #贪心，就正向找
        maxIndex=0
        for i in range(len(nums)):
            if maxIndex<i:
                return False
            currentMaxIndex=nums[i]+i
            if maxIndex<currentMaxIndex:
                maxIndex=currentMaxIndex
            if maxIndex>=len(nums)-1:
                return True
        return False

