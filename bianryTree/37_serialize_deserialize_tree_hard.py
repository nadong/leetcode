"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        def serialize_dfs(root):
            if not root:
                res.append("null")
                return
            res.append(root.val)
            serialize_dfs(root.left)
            serialize_dfs(root.right)
        serialize_dfs(root)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return []

        index = [0]
        def deserialize_dfs(data):
            if data[index[0]] == "null":
                index[0] += 1
                return None
            node = TreeNode(data[index[0]])
            index[0] += 1
            node.left = deserialize_dfs(data)
            node.right = deserialize_dfs(data)
            return node
        return deserialize_dfs(data)





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))