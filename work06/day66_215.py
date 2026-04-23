# ============================================
# @File    : day66_215.py
# @Date    : 2026-04-22 20:00
# @Author  : 帅宇昕
# ============================================
import heapq
import random
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # hp=[10*-4-1]*k
    #     # for i in range(k):
    #
    #
    #     hp=[]
    #     for i in range(k):
    #         heapq.heappush(hp,nums[i])
    #     for i in range(k,len(nums)):
    #         heapq.heappush(hp,nums[i])
    #         heapq.heappop(hp)
    #     k=heapq.heappop(hp)
    #     return k

#---------------------------------
    # def myheapdify(self, hp, k,i):
    #     #这里使用下沉法
    #     #需要判断，当前节点和左右节点哪一个大
    #     minst=i
    #     left=2*i+1
    #     right=2*i+2
    #     if left<k and hp[left]<hp[minst]:
    #         minst=left
    #     if right<k and  hp[right]<hp[minst]:
    #         minst=right
    #     if minst != i:
    #         hp[minst],hp[i]=hp[i],hp[minst]
    #         self.myheapdify(hp,k,minst)
    #
    # def build_min_heap(self,nums,k):
    #     n=k//2
    #     for i in range(n-1,-1,-1):
    #         self.myheapdify( nums, k,i)
    #     return nums
    #
    #
    #
    #
    # def myheadpushAndPop(self, hp,k,number):
    #
    #     if number>hp[0]:
    #         hp[0]=number
    #         self.myheapdify(hp, k, 0)
    #         return hp[0]
    #     else:
    #
    #         return number
    #
    # def getTop(self, hp):
    #     return  hp[0]
    #
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     hp=self.build_min_heap(nums[:k], k)
    #     for i in range(k,len(nums)):
    #         self.myheadpushAndPop(hp,k,nums[i])
    #         # print(hp)
    #     return self.getTop(hp)


#-----------------------------------------

    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSearch(nums,l,r,k):
            if l==r:

                return nums[l]

            left=l
            right=r
            pivot_index = random.randint(l, r)
            nums[l], nums[pivot_index] = nums[pivot_index], nums[l]
            pivot=nums[l]
            while left<right:
                while left<right and pivot <=nums[right]:
                    right-=1
                while left<right and pivot >=nums[left]:
                    left+=1

                if left<right:
                    nums[left],nums[right]=nums[right],nums[left]
            nums[l], nums[right] = nums[right], nums[l]
            if k==right:
                return nums[right]
            elif l<=k<right:
                return quickSearch(nums, l, right-1, k)
            elif right<k<=r:
                return quickSearch(nums, right+1 , r, k)





        return quickSearch(nums,0,len(nums)-1,len(nums)-k)


