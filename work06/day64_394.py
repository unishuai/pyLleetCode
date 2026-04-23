# ============================================
# @File    : day64_394.py
# @Date    : 2026-04-22 10:12
# @Author  : 帅宇昕
# ============================================
class Solution:
    def decodeString(self, s: str) -> str:
        #像这种配对的，可以使用堆栈，因为堆栈可以按照顺序存储中间状态
        stack=[]
        res=""
        count=0
        needDecodeString = ""
        for i in range(len(s)):

            if s[i] =='[':
                count+=1
                stack.append(s[i])

            elif s[i] ==']':


                while stack:
                    p = stack.pop()
                    if p == '[':
                        count-=1
                        break
                    else:
                        needDecodeString = p + needDecodeString
                #这里的话也是需要一直迭代，然后吧数字找完
                times=""
                while stack:
                    p = stack[-1]
                    if ord("0")<=ord(p)<=ord("9"):
                        times=p+times
                        stack.pop()
                    else:
                        break

                times = int(times)


                if count==0:

                    res = res + times * needDecodeString
                    needDecodeString=""
                else:
                    #这里的话就得按照顺序个加进去，或者直接整个push我觉得也没问题
                    current=times * needDecodeString
                    for k in current:
                        stack.append(k)
                    needDecodeString = ""
            elif count>0 or ord("0")<=ord(s[i])<=ord("9"):
                stack.append(s[i])
            else:
                res += s[i]



        # prefixStr=""
        # while stack:
        #     p=stack.pop()
        #     prefixStr=p+prefixStr
        # res=prefixStr+res
        return res

    # def decodeString(self, s: str) -> str:
    #     stack=[]
    #     res=''
    #     times=''
    #     strp=''
    #     for i in range(len(s)):
    #         if s[i] =='[':
    #             stack.append(strp)
    #             strp = ''
    #             stack.append(times)
    #             times=''
    #
    #             # stack.append(s[i])
    #
    #
    #         elif ord("0")<=ord(s[i])<=ord('9'):
    #             times+=s[i]
    #         elif ord('a')<=ord(s[i])<=ord('z'):
    #             strp+=s[i]
    #         elif s[i]==']':
    #             # 括号里面的数据
    #             times=stack.pop()
    #             strp=strp*int(times)
    #             lastStrp=stack.pop()
    #             strp=lastStrp+strp
    #             times=""
    #
    #
    #     return strp




