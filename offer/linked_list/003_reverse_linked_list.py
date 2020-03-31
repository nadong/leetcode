class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
# stack
def printListFromTailToHead(listNode):
	stack = []
	result_array = []
	node_p = listNode
	while node_p:
		stack.append(node_p.val)
		node_p = node_p.next

	while stack:
		result_array.append(stack.pop(-1))

	return result_array

# 本身栈调用

result_array=[]
def printListFromTailToHead2(listNode):
	if listNode:
		printListFromTailToHead2(listNode.next)
		result_array.append(listNode.val)
	return result_array
		

