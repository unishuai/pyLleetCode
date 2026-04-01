# ============================================
# @File    : day03_15.py.py
# @Date    : 2026-03-26 17:13
# @Author  : 帅宇昕
# ============================================
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #这里有一个n方复杂度的解法
        nums=sorted(nums)
        print(nums)
        # res=set()
        res = list()

        for i in range(len(nums)):
            k = len(nums) - 1
            if nums[i]==nums[i-1] and i-1>=0:
                continue
            for j in range(i+1,len(nums)):
                if nums[j] == nums[j - 1] and  j>=i+2:
                    continue

                while nums[i]+nums[j]+nums[k]>0 and j<k:
                    k-=1
                if j<k:
                    if nums[i]+nums[j]+nums[k]==0:
                        arr=[nums[i],nums[j],nums[k]]
                        # res.add(arr)
                        res.append(arr)
        # return list(res)
        return res









a=[-1,0,1,2,-1,-4]
test=Solution()
test.threeSum(a)
