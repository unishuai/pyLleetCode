# ============================================
# @File    : day61_153.py
# @Date    : 2026-04-21 15:49
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    #我这个解法只能说是侥幸答对了，因为初始化为nums[0],刚好可以处理没有移动的情况
    # def findMin(self, nums: List[int]) -> int:
    #     #这个和找到目标值应该是属于同一个类型的问题
    #     l=0
    #     r=len(nums)-1
    #     res=nums[0]
    #     while l<=r:
    #         mid=(l+r)//2
    #         #先判断nums取值取的是哪一个区间
    #         res=min(res,nums[mid])
    #         if nums[0]<=nums[mid]:
    #             #mid取值在左边较大的位置，我们是寻找最小值，没话说，直接l=mid+1
    #             l = mid + 1
    #         else:
    #             #nums[0] <= nums[mid]
    #             #他这个右边是有序递增的，左边就是先增后可能减
    #             r=mid-1
    #
    #     return res

    def findMin(self, nums: List[int]) -> int:
        #这个和找到目标值应该是属于同一个类型的问题
        l=0
        r=len(nums)-1
        res=nums[0]
        while l<=r:
            mid=(l+r)//2
            #先判断nums取值取的是哪一个区间
            res=min(res,nums[mid])
            if nums[-1]<nums[mid]:
                #mid取值在左边较大的位置，我们是寻找最小值，没话说，直接l=mid+1
                l = mid + 1
            else:
                #nums[0] <= nums[mid]
                #他这个右边是有序递增的，左边就是先增后可能减
                r=mid-1

        return l




