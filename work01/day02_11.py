# ============================================
# @File    : day02_11.py.py
# @Date    : 2026-03-24 16:37
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #边界问题，分析清楚问题，理解内在原理，然后进行处理
        rightIndex=len(height)-1
        leftIndex=0
        #每次移动最短边界，因为接下来不管怎么移动，最满的情况就是最小边界
        rightLength=height[rightIndex]
        leftLength=height[leftIndex]
        maxWater =0
        while leftIndex<rightIndex:
            minLength=min(leftLength,rightLength)
            width=rightIndex-leftIndex
            currentMaxWater= minLength*width
            maxWater=max(maxWater,currentMaxWater)
            if leftLength < rightLength:
                leftIndex+=1
            else:
                rightIndex-=1
            rightLength = height[rightIndex]
            leftLength = height[leftIndex]
        return maxWater