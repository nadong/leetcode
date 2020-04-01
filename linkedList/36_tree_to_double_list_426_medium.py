"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

"""
class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        def inorder(node=root):
            if node:
                inorder(node.left)
                if not self.pre:
                    self.head = node
                else:
                    self.pre.right, node.left = node, self.pre
                self.pre = node
                inorder(node.right)
        inorder(root)
        self.pre.right, self.head.left = self.head, self.pre
        return self.head