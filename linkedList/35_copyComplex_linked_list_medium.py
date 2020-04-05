"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
“”“第一部分”“”
def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
“”“第二部分”“”
            copy.random = dfs(head.random)
            return copy
首先反复运行第一部分，copy.next = dfs(head.next) 会递归得越来越深，，当 碰到 head == None 时，开始运行第二部分，准备从尾结点回溯；
回溯时，先从尾结点开始回溯：调用dfs(head.random)时，由于结点都保存在了哈希表中，因此 return visited[head]，这时完成random指针，完成了最后一个结点，故return copy。再进行倒数第二个结点的回溯：调用dfs(head.random)，return visited[head]，return copy.......
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy

        visited = {}
        return dfs(head)