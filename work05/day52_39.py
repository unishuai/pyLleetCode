# ============================================
# @File    : day52_39.py
# @Date    : 2026-04-19 16:40
# @Author  : 帅宇昕
# ============================================

from typing import List, Counter


class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res=[]
    #     combainations=[]
    #     # 这种深度优先递归也是不能够往回走的，限制他组合的唯一性，就是它的index一直要往右走
    #     def dfs(candidates,index,target):
    #         if index==len(candidates) or target<0:
    #             return 0
    #         if target==0:
    #             res.append(combainations[:])
    #             return
    #
    #
    #         for i in range(index,len(candidates)):
    #             currentTarget=target - candidates[i]
    #             combainations.append(candidates[i])
    #             dfs(candidates, i, currentTarget)
    #             combainations.pop()
    #
    #     index=0
    #     dfs(candidates,index,target)
    #     return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        combainations=[]
        # 这种深度优先递归也是不能够往回走的，限制他组合的唯一性，就是它的index一直要往右走
        def dfs(candidates,index,target):
            if index==len(candidates) or target<0:
                return 0
            if target==0:
                res.append(combainations[:])
                return
            dfs(candidates, index+1, target)

            currentTarget = target - candidates[index]
            combainations.append(candidates[index])
            dfs(candidates, index, currentTarget)
            combainations.pop()

            # for i in range(index,len(candidates)):
            #     currentTarget=target - candidates[i]
            #     combainations.append(candidates[i])
            #     dfs(candidates, i, currentTarget)
            #     combainations.pop()

        index=0
        dfs(candidates,index,target)
        return res
