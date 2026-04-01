import collections
# ============================================
# @File    : day08_239.py
# @Date    : 2026-03-31 20:32
# @Author  : 帅宇昕
# ============================================
import heapq
from typing import List


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     "使用优先队列或者堆的方式解决"
    #     n=len(nums)
    #     q=[(-nums[i],i) for i in range(k)]
    #     heapq.heapify(q)
    #     ans = [-q[0][0]]
    #     for i in range(k,n):
    #         heapq.heappush(q,(-nums[i],i))
    #         while q[0][1]<=i-k:
    #             heapq.heappop(q)
    #         ans.append(-q[0][0])
    #     return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=collections.deque()
        n=len(nums)
        # q.append((nums[0], 0))
        for i in range(k):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k,n):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
            while i-k>=q[0]:
                q.popleft()
            ans.append(nums[q[0]])
        return ans













