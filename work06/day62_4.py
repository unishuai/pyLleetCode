# ============================================
# @File    : day62_4.py
# @Date    : 2026-04-21 16:49
# @Author  : 帅宇昕
# ============================================
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        leftCha={'(','{','['}
        mp={'(':')','[':']','{':'}'}

        for i in range(len(s)):
            if s[i] in leftCha:
                stack.append(s[i])
            else:
                if stack :
                    p=stack.pop()
                    if mp[p]!=s[i]:
                        return False
                else:
                    return False

        if stack:
            return False
        return True