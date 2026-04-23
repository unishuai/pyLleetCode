# ============================================
# @File    : day65_739.py
# @Date    : 2026-04-22 16:16
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(0,len(temperatures)):
            if len(stack)==0 or stack[-1][0]>=temperatures[i]:
                #里面没有温度或者，是降温了
                stack.append((temperatures[i],i))
            elif stack[-1][0]<temperatures[i]:
                count=0
                while stack and stack[-1][0]<temperatures[i]:
                    count+=1
                    p,index=stack.pop()
                    res[index]=i-index
                stack.append((temperatures[i], i))
        return res


