# ============================================
# @File    : day05_3.py
# @Date    : 2026-03-27 17:43
# @Author  : 帅宇昕
# ============================================
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxSub=0
        lastSub=0
        currentSub=0
        buckets=set()
        for i in range(len(s)):
            if lastSub >0:
                buckets.remove(s[i - 1])
                currentSub = lastSub-1
            for j in range(i+currentSub, len(s)):
                if s[j] not in buckets:
                    currentSub += 1
                    buckets.add(s[j])
                else:
                    break
            lastSub = currentSub
            maxSub=max(currentSub,maxSub)
        return maxSub





            # if lastSub <= 1:
            #     if lastSub ==1:
            #
            #
            #     currentSub=0
            #     for j in range(i,len(s)):
            #         if j not in buckets:
            #             currentSub+=1
            #             buckets.add(s[j])
            #         else:
            #             lastSub=currentSub
            #             break
            #
            #
            # else:
            #     buckets.remove(s[i-1])
            #     currentSub = lastSub-1
            #     for j in range(i,len(s)):
            #         if j not in buckets:
            #             currentSub+=1
            #             buckets.add(s[j])
            #         else:
            #             lastSub=currentSub
            #             break
            #














t=Solution()
s=t.lengthOfLongestSubstring("abcabcbb")
print(s)

