# ============================================
# @File    : day50_78.py
# @Date    : 2026-04-19 14:18
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res=[]
    #     tmplist=[]
    #     def dfs(nums,index,depth,times):
    #         if depth==times:
    #             res.append([ i for i in tmplist])
    #             return
    #         if len(nums) -index<times-depth:
    #             return
    #
    #
    #         for i in range(index,len(nums)):
    #             tmplist.append(nums[i])
    #             #这里一直往右探索就好了
    #             dfs(nums, i+1,depth+1, times)
    #             tmplist.pop()
    #
    #
    #
    #     index=0
    #
    #     depth=0
    #     for times in range(len(nums)+1):
    #         dfs(nums, index,depth, times)
    #     return res

    #子集的话就从定义出发，选或者不选
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        tmplist = []
        def dfs(nums,cur):
            if cur==len(nums):
                res.append(tmplist[:])
                return

            dfs(nums, cur + 1)
            tmplist.append(nums[cur])
            dfs(nums,cur + 1)
            tmplist.pop()



        cur=0

        dfs(nums,cur)
        return res

