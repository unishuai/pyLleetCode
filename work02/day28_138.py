# ============================================
# @File    : day28_138.py
# @Date    : 2026-04-13 16:47
# @Author  : 帅宇昕
# ============================================

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     # 深拷贝的单点是这个random肯定不是说按照顺序就能来的
    #     # 每一次重新查找也不是很合适，用map字典类型存储，然后更新
    #     nodeMap=dict()
    #     p=head
    #     while p!=None:
    #         nodeMap[p]=Node(p.val)
    #         p=p.next
    #     p = head
    #
    #     while p!=None:
    #         q=nodeMap.get(p)
    #         q.next=nodeMap.get(p.next)
    #         q.random = nodeMap.get(p.random)
    #         p=p.next
    #     return nodeMap.get(head)

    nodeMap = dict()
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 深拷贝的单点是这个random肯定不是说按照顺序就能来的
        # 每一次重新查找也不是很合适，用map字典类型存储，然后更新

        if head is None  :
            return head
        if head  not in self.nodeMap:
            self.nodeMap[head]=Node(head.val)
            self.nodeMap[head].next=self.copyRandomList(head.next)
            self.nodeMap[head].random=self.copyRandomList(head.random)

        return self.nodeMap[head]

