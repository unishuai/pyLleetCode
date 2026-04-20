# ============================================
# @File    : day51_17.py
# @Date    : 2026-04-19 15:51
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        res=[]
        tmplist=[]
        def dfs(digits, index):
            if index==len(digits):
                res.append("".join(tmplist))
                return
            p=digits[index]
            cha=mp[p]
            for i in cha:
                tmplist.append(i)
                dfs(digits,index+1)
                tmplist.pop()


        index=0
        dfs(digits,index)
        return res

