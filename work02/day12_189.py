# ============================================
# @File    : day12_189.py
# @Date    : 2026-04-01 21:34
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     nlen = len(nums)
    #     k=k%nlen
    #     tmp=[0]*k
    #
    #     for i in range(nlen-k,nlen):
    #         tmp[i-nlen+k]=nums[i]
    #     for i in range(nlen-k-1,-1,-1):
    #         nums[i+k]=nums[i]
    #     for i in range(0,k):
    #         nums[i]=tmp[i]
    #     print(nums)
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = self.gcd(k, n)
        for start in range(count):
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                temp = nums[next_idx]
                nums[next_idx] = prev
                prev = temp
                current = next_idx

                if current == start:
                    break

    def gcd(self, x: int, y: int) -> int:
        return self.gcd(y, x % y) if y > 0 else x




t=Solution()
t.rotate(nums = [1,2,3,4,5,6,7], k = 3)