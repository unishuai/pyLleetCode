# ============================================
# @File    : day70_45.py
# @Date    : 2026-04-23 14:50
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     nlen=len(nums)
    #     minStep=[10000]*nlen
    #     minStep[0]=0
    #     for i in range(nlen):
    #         dist=nums[i]
    #         maxdist=min(dist+i+1,nlen)
    #         laststep=minStep[i]
    #         for j in range(i+1,maxdist):
    #             minStep[j]=min(laststep+1,minStep[j])
    #
    #     return minStep[-1]

    def jump(self, nums: List[int]) -> int:
        nlen=len(nums)
        step=0
        end=0
        maxPostion=0
        #因为如果能到最后一个位置i，可能最后一个位置就是end
        for i in range(nlen-1):
            maxPostion=max(maxPostion,i+nums[i])
            if i==end:
                end=maxPostion
                step+=1
        return step