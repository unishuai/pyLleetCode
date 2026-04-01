# ============================================
# @File    : day06_428.py
# @Date    : 2026-03-28 15:52
# @Author  : 帅宇昕
# ============================================
from typing import List


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#
#         res=[]
#         plen=len(p)
#         heirent=0
#         tmp = list(p)
#         for i in range(len(s)):
#
#             for j in range(0+heirent,plen):
#                 if i+j>=len(s):
#                     break
#
#
#                 if s[i+j] in tmp:
#                     tmp.remove(s[i+j])
#                     heirent+=1
#                     if len(tmp) == 0:
#                         res.append(i)
#                         tmp.append(s[i])
#                         heirent -=1
#                         break
#                 else:
#                     if heirent>0:
#                         tmp.append(s[i])
#                         heirent-=1
#
#                     else:
#                         tmp = list(p)
#                         heirent=0
#                     break
#
#         return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len<p_len:
            return []
        res = []
        count=[0]*26
        for i in range(p_len):
            count[ord(s[i])-97]+=1
            count[ord(s[i])-97]-=1
        differ = [c != 0 for c in count].count(True)
        if differ == 0:
            res.append(0)
        for i in range(s_len-p_len):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                differ+=1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            if differ == 0:
                res.append(i + 1)

            return res


t=Solution()
print(t.findAnagrams(s = "cbaebabacd", p = "abc"))