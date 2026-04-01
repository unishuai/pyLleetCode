# ============================================
# @File    : day09_76.py
# @Date    : 2026-04-01 10:40
# @Author  : 帅宇昕
# ============================================
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tlen=len(t)
        slen=len(s)
        if tlen>slen:
            return ""
        charMap=dict()
        for chr in t:
            # charMap.setdefault()
            charMap[chr]=charMap.get(chr,0)-1
        # print(charMap)
        count=0
        sIndex=0
        # eIndex=0
        sMin = -1
        eMin = slen
        for i in range(slen):
            if s[i] in charMap and charMap[s[i]] <0:
                # 说明增加的是需要匹配的字符串，然后满足了其中一个条件
                charMap[s[i]]  += 1
                count +=1
                if count==tlen:
                    eIndex=i
                    # print(111111)
                    #说明这个字符串里面找到存在一个子串，最右端为s[i]的时候，符合要求
                    #这时候就缩短左边，看看缩短之后，最短是多少
                    while charMap[s[sIndex]]>0:
                        charMap[s[sIndex]]=charMap[s[sIndex]]-1
                        sIndex+=1
                    if eIndex-sIndex<eMin-sMin:
                        sMin = sIndex
                        eMin=eIndex

                    count -= 1
                    charMap[s[sIndex]]-=1
                    sIndex+=1
            elif s[i] in charMap:
                charMap[s[i]]  += 1
            else:
                charMap[s[i]]=1
        # print(sMin)
        # print(eMin)
        if sMin==-1:
            return ""
        return s[sMin:eMin+1]





t=Solution()
print(t.minWindow(s="ADOBECODEBANC", t="ABC"))