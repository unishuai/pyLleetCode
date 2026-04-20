# ============================================
# @File    : day56_51.py
# @Date    : 2026-04-20 20:06
# @Author  : 帅宇昕
# ============================================
import math
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # N皇后问题的规则是不能再同一列，不能再同一行
        # 也就是说每一个皇后可以在X和Y中都任选一个落子
        # 然后判断他们是否在一个对角线上,判断方式就是两个点相减，绝对值相等
        x=[ i for i in range(n)]
        visitedx=[0 for i in range(n)]
        y=[ i for i in range(n)]
        visitedy = [0 for i in range(n)]
        res=[]
        tmplist=[]
        point="."
        queen='Q'


        def dfs(depth,n):
            if depth==n:
                # print(111)
                graph=[ ['.']*n for i in range(n)]
                for x,y in tmplist:
                    graph[x][y]="Q"


                res.append(["".join(graph[i]) for  i in range(n)])

                return
            #找X
            # for i in range(depth,n):
            #     if visitedx[i] == 0:
            #
                # 找J分开找效率更高
            i=depth
            for j in range(n):
                if visitedy[j] == 0:
                    # 判断是不是能添加
                    cando = True
                    for qx, qy in tmplist:
                        if abs(qx - i) == abs(qy - j):
                            # 说明这个点不合适，尝试下一个
                            cando = False
                            break

                    if cando:
                        tmplist.append((i, j))
                        # 说明这一个点没有人落子
                        visitedx[i] = 1
                        visitedy[j] = 1
                        dfs(depth + 1, n)
                        visitedx[i] = 0
                        visitedy[j] = 0
                        tmplist.pop()




        depth=0
        dfs(depth,n)
        return res

