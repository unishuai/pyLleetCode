# ============================================
# @File    : day07_560.py
# @Date    : 2026-03-31 19:22
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        注意，这里的非空子数组连续
        :param nums:
        :param k:
        :return:
        """
        prefixMap=dict()
        prefixMap[0]=1
        prefix=0
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix-k in prefixMap:
                # prefixMap[k-prefix]+=prefixMap[k-prefix]
                count +=prefixMap[prefix-k]
            prefixMap[prefix]=prefixMap.get(prefix, 0) + 1
        return count
