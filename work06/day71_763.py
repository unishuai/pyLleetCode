# ============================================
# @File    : day71_763.py
# @Date    : 2026-04-23 15:39
# @Author  : 帅宇昕
# ============================================
# s = "ababcbaca defegde hijhklij"
from typing import List


class Solution:
    # def partitionLabels(self, s: str) -> List[int]:
    #     # 如果不是题目告诉我是贪心，我也真的项目到
    #     # 找到一个值，就确定右区间
    #     # 然后继续走，碰到之前寻找过得值就跳过
    #     # 碰到的是没有寻找过得值，就开始在右区间+1的地方开始遍历
    #     mp={}
    #     res=[]
    #     lastRightIndex=-1
    #     rightIndex=0
    #     nlen=len(s)
    #     for i in  range(nlen):
    #         if i >rightIndex:
    #             #如果超出边界了就添加进去，新建立一个边界
    #             res.append(rightIndex-lastRightIndex)
    #             lastRightIndex=rightIndex
    #             rightIndex=i
    #         searRight=s[i]
    #         if searRight not in mp:
    #             findIndex=i
    #             for j in range(nlen-1,i,-1):
    #                 #这里倒着查，查到了就可以break
    #                 if s[j] ==searRight:
    #                     findIndex=j
    #                     break
    #             mp[searRight]=findIndex
    #             rightIndex=max(findIndex,rightIndex)
    #     res.append(rightIndex-lastRightIndex)
    #     return res

    def partitionLabels(self, s: str) -> List[int]:
        last=[0]*26
        slen=len(s)
        for i in range(slen):
            last[ord(s[i])-ord('a')]=i

        lastmaxright=-1
        maxright=0
        res=[]
        for i in range(slen):
            if i >maxright:
                res.append(maxright-lastmaxright)
                lastmaxright=maxright
                maxright=i
            currentmaxright=last[ord(s[i])-ord('a')]
            maxright=max(currentmaxright,maxright)
        res.append(maxright-lastmaxright)
        return res


