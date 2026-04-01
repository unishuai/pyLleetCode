# ============================================
# @File    : day11_56.py
# @Date    : 2026-04-01 21:03
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        mergeList=[]

        left = intervals[0][0]
        right = intervals[0][1]

        for i in range(1,len(intervals)):


            #分为四种情况
            # a2>b1 ,说明有交集
            if  right>=intervals[i][0]:
                left=min(left,intervals[i][0])
                right=max(right,intervals[i][1])

            # a2<b1，一个在左边，一个在右边
            else:
                mergeList.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]

        mergeList.append([left,right])
        return mergeList



t=Solution()
print(t.merge(intervals=[[8, 10], [15, 18], [1, 3], [2, 6], ]))