# ============================================
# @File    : day54_79.py
# @Date    : 2026-04-19 20:33
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(rindex,lindex,board,visted,index,word):

            if rindex<0 or rindex>=len(board) or lindex<0 or lindex>=len(board[0]) or visted[rindex][lindex]==1 or board[rindex][lindex]!=word[index]:
                return False

            if board[rindex][lindex]==word[index]:
                visted[rindex][lindex]=1
                index+=1

                if index == len(word) :
                    visted[rindex][lindex] = 0
                    return True
                up=dfs(rindex-1, lindex, board, visted, index, word)
                down=dfs(rindex+1, lindex, board, visted, index, word)
                left=dfs(rindex , lindex-1, board, visted, index, word)
                right=dfs(rindex , lindex+1, board, visted, index, word)
                visted[rindex][lindex] = 0
                return up or down or left or right




        row=len(board)
        line=len(board[0])
        index=0

        visted = [[0] * line for _ in range(row)]
        for i in range(row):
            for j in range(line):
                if board[i][j]==word[index]:
                    # print("进入判断i={0},j={1}".format(i,j))
                    isfind=dfs(i,j,board,visted,index, word)
                    if isfind:
                        return True
        return False


t=Solution()
print(t.exist(board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"))