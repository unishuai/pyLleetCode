# ============================================
# @File    : day14_41.py
# @Date    : 2026-04-02 10:28
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     #向这种这种没有规律的可以用集合
    #     nums=set(nums)
    #     res=-1
    #     i=1
    #     while res==-1:
    #         if i not in nums:
    #             res=i
    #             break
    #         i+=1
    #     return res

    def firstMissingPositive(self, nums: List[int]) -> int:

        nlen=len(nums)
        #全部修改成正数
        for i in range(nlen):
            if nums[i]<=0 :
                nums[i]=nlen+1

        for i in range(nlen):
            num = abs(nums[i])
            if num <= nlen:
                nums[num-1]=-abs(nums[num-1])

        for i in range(nlen):
            if nums[i] > 0:
                return i + 1
        return nlen + 1






