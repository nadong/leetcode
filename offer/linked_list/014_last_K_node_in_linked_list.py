class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 快慢指针， 快指针提前走K 步，然后 当快指针走到tail的时候， return slow_p
def FindKToTail(head, k):
    if not head:
        return None
    fast_p = head
    slow_p = head
    for _ in range(k):
        if fast_p:
            fast_p = fast_p.next
        else:
            return None

    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next

    return slow_p