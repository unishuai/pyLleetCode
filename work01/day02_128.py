# ============================================
# @File    : day02_128.py.py
# @Date    : 2026-03-24 15:44
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted=sorted(nums)
        # arr =
        #这个题目需要每为log(n)的复杂度，那就是不能排序,也不能所有值都去比较，这样子的话
        #使用哈希表或者dp会好一点
        datas=set(nums)
        historyMax=0
        for num in datas:
            if num -1 not in datas:
                #只有他是最小值的时候，才开始循环匹配
                currentMax=1
                currentNum=num+1
                while currentNum in datas:
                    currentMax+=1
                    currentNum+=1
                historyMax= currentMax if currentMax>historyMax  else historyMax
        return historyMax