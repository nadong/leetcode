# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
1) 统计linked link 长度，然后找到 n-k 个点
2） 如下
"""
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        former, latter = head, head

        for _ in range(k):
            former = former.next

        while former:
            former, latter = former.next, latter.next

        return latter
