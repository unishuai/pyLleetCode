# ============================================
# @File    : day68_121.py
# @Date    : 2026-04-23 10:01
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # arr=[0]*len(prices)
        maxPrice=prices[-1]
        res=0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>maxPrice:
                maxPrice=prices[i]
            # arr[i]=maxPrice
            res=max(res,maxPrice-prices[i])
        return res


