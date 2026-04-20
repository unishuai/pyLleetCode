# ============================================
# @File    : day49_46.py
# @Date    : 2026-04-19 11:53
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def __init__(self):
    #     self.res = []
    #     self.tmplist = []
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #
    #     def dfs(nums,index,visted):
    #         if  visited[index]==1:
    #             return
    #
    #         visited[index]=1
    #         self.tmplist.append(nums[index])
    #         isEnd=True
    #         for i in range(len(nums)):
    #             if visited[i]==0:
    #                 isEnd=False
    #                 dfs(nums, i, visted)
    #
    #         if isEnd is True:
    #             path = [i for i in self.tmplist]
    #             self.res.append(path)
    #
    #         self.tmplist.pop()
    #
    #         visited[index] = 0
    #
    #     visited=[0]*   len(nums)
    #     for i in range(len(nums)):
    #
    #         dfs(nums,i,visited)
    #     return self.res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(nums, depth):
            if depth ==len(nums)-1:
                #保存数据
                res.append([i for i in nums])
            #这里相当于是把第depth的位置拍好序号
            for i in range(depth,len(nums)):
                tmp=nums[depth]
                nums[depth]=nums[i]
                nums[i]=tmp
                dfs(nums,depth+1)
                tmp = nums[depth]
                nums[depth] = nums[i]
                nums[i] = tmp




        nlen=len(nums)
        depth=0
        dfs(nums,depth)
        return res

