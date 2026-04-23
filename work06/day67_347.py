# ============================================
# @File    : day67_347.py
# @Date    : 2026-04-23 9:14
# @Author  : 帅宇昕
# ============================================
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #不管怎样，应该都需要遍历一轮，统计处每一个位置的个数
        mp=collections.defaultdict(int)
        for i in nums:
            if i in mp:
                mp[i]=mp[i]+1
            else:
                mp[i]=1
        toplist=[]
        count=0
        for key in mp:
            count+=1

            heapq.heappush(toplist,[mp[key],key])
            if count > k:
                heapq.heappop(toplist)


        res=[]
        for i in range(k):
            res.append(heapq.heappop(toplist)[1])
        return res