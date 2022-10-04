# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

import collections


class Codec:
    def serialize(self, root):
        # 层序遍历
        if root == None:return 
        stack = collections.deque()
        stack.append(root)
        ret = str(root.val)
        while stack:
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
                ret += ',' + str(node.left.val)
            else: ret += ',N'
            if node.right:
                stack.append(node.right)
                ret += ',' + str(node.right.val)
            else: ret += ',N'
        return ret
        

    def deserialize(self, data):
        if data == None: return None
        data = data.split(',')
        # 层序建立树
        root = TreeNode(int(data[0]))
        stack = collections.deque()
        stack.append(root)
        index = 1
        while stack:
            node = stack.popleft()
            left = data[index]
            if left != 'N':
                node.left = TreeNode(int(left))
                stack.append(node.left)
            index += 1
            right = data[index]
            if right != 'N':
                node.right = TreeNode(int(right))
                stack.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
root = TreeNode(-1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
codec = Codec()
codec.deserialize(codec.serialize(root))