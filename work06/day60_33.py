# ============================================
# @File    : day60_33.py
# @Date    : 2026-04-21 10:22
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     l=0
    #     r=len(nums)-1
    #     def binarySearch(nums,l,r,target)->int:
    #         if l>r:
    #             return -1
    #         if l==r:
    #             if nums[l]==target:
    #                 return l
    #             else:
    #                 return -1
    #         #这里就是l<r
    #         mid=(l+r)//2
    #         if nums[l]<nums[r]:
    #             if target<nums[l] or target>nums[r]:
    #                 return -1
    #             if nums[mid]==target:
    #                 return mid
    #             elif nums[mid]>target:
    #                 return binarySearch(nums, l, mid-1, target)
    #             else:
    #                 return binarySearch(nums, mid+1, r, target)
    #         elif nums[l]>nums[r]:
    #             #这个继续往后面分
    #
    #             lfind=binarySearch(nums, l, mid, target)
    #             rfind=binarySearch(nums, mid+1, r, target)
    #             if lfind!=-1:
    #                 return lfind
    #             elif rfind !=-1:
    #                 return rfind
    #             return -1
    #
    #
    #
    #
    #
    #
    #
    #     return binarySearch(nums,l,r,target)

    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid=(l+r)//2
            #先判断是不是直接找到了
            if nums[mid]==target:
                return mid

            if nums[0] <= nums[mid]:
                 #这个就是一说mid是在Nums右边的正常值
                if nums[0]>target or nums[mid]<target  :
                    l=mid+1
                else:
                    r=mid-1
            else:
                #这边的Mid就是取到了平移过去的较小的值中,或者nums[0]>target,自能在mid左侧
                if nums[0]<=target or nums[mid]>target:
                    r=mid-1
                #下面这里就是或者nums[0]>target,自能在mid左侧
                elif nums[mid]<target:
                    l=mid+1
        return -1




