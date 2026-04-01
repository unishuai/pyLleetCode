# ============================================
# @File    : day04_42.py
# @Date    : 2026-03-27 10:38
# @Author  : 帅宇昕
# ============================================
from typing import List


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         rIndex = len(height)-1
#         lIndex = 0
#
#         sumWater=0
#         tmpWaterHeight=0
#         while lIndex<rIndex:
#             sumWater -= min(height[lIndex],height[rIndex], tmpWaterHeight)
#
#
#
#             minHeight=min(height[lIndex],height[rIndex])
#             #算增加的水（体积在循环之前已经减去）
#             if minHeight > tmpWaterHeight:
#                 width = rIndex - lIndex - 1
#                 sumWater +=width*(minHeight-tmpWaterHeight)
#                 tmpWaterHeight=minHeight
#
#             if height[lIndex] <height[rIndex]:
#
#                 lIndex+=1
#                 # if height[lIndex] <= tmpWaterHeight:
#
#
#             else:
#                 rIndex -= 1
#
#                 # tmpWaterHeight-=min(height[lIndex],tmpWaterHeight)
#         # print(sumWater)
#         return sumWater
#
# a=Solution()
# a.trap([0,1,0,2,1,0,1,3,2,1,2,1])


class Solution:
    def trap(self, height: List[int]) -> int:
        rIndex = len(height)-1
        lIndex = 0

        sumWater=0
        tmpWaterHeight=0
        while lIndex<rIndex:
            sumWater -= min(height[lIndex],height[rIndex], tmpWaterHeight)



            minHeight=min(height[lIndex],height[rIndex])
            #算增加的水（体积在循环之前已经减去）
            if minHeight > tmpWaterHeight:
                width = rIndex - lIndex - 1
                sumWater +=width*(minHeight-tmpWaterHeight)
                tmpWaterHeight=minHeight

            if height[lIndex] <height[rIndex]:

                lIndex+=1
                # if height[lIndex] <= tmpWaterHeight:


            else:
                rIndex -= 1

                # tmpWaterHeight-=min(height[lIndex],tmpWaterHeight)
        # print(sumWater)
        return sumWater