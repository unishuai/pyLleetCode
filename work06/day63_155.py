# ============================================
# @File    : day63_155.py
# @Date    : 2026-04-21 22:58
# @Author  : 帅宇昕
# ============================================
class MinStack:

    def __init__(self):
        self.data=[]
        self.minstack=[]

    def push(self, val: int) -> None:

        self.data.append(val)
        if len(self.minstack)==0 or self.minstack[-1]>=val  :
            # print(1)
            self.minstack.append(val)

    def pop(self) -> None:
        if self.data:
            p=self.data.pop()
            if p == self.minstack[-1]:
                self.minstack.pop()





    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

param_3 = obj.top()
param_4 = obj.getMin()