# ============================================
# @File    : day53_22.py
# @Date    : 2026-04-19 19:07
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 有效括号满足的条件
        # 结束时，左括号和右括号数量要相等
        # 中途要满足左括号大于等于右括号
        res=[]
        parents=[]
        def dfs(left,right):
            if left==0 and right==0:
                res.append(''.join(parents))
                return
            lstr='('
            rstr=')'
            if 0<left<right:

                parents.append(lstr)
                dfs(left-1,right)
                parents.pop()


                parents.append(rstr)
                dfs(left , right-1)
                parents.pop()
            elif 0<left and left==right:
                parents.append(lstr)
                dfs(left - 1, right)
                parents.pop()
            elif 0 == left and 0< right:
                parents.append(rstr)
                dfs(left, right - 1)
                parents.pop()






        left=n
        right=n
        dfs(left,right)
        return res
