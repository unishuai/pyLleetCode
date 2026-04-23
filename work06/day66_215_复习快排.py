# # ============================================
# # @File    : day66_215_复习快排.py
# # @Date    : 2026-04-22 21:56
# # @Author  : 帅宇昕
# # ============================================
class Solution:
    def quick_sort(self, nums):
        def sort(nums,l,r):
            if l>=r:
                return
            judge=nums[l]
            i,j=l,r
            while i<j:
                while i<j and judge<=nums[j]:
                    j-=1
                # nums[j]<judge 或者i=j
                while i<j and judge>=nums[i]:
                    i+=1
                # nums[i]>judge 或者i=j
                # nums[i],nums[j]=nums[j],nums[i]
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            sort(nums, l, j-1)
            sort(nums, j+1,r)


        sort(nums,0, len(nums) - 1)
        return nums



nums = [3, 6, 8, 10, 1, 2, 1]
s = Solution()
print(s.quick_sort(nums))