# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        ret = []
        if not root: return '*'
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                ret.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                ret.append(None)
        # string
        s = ','.join(map(str, ret))
        return s
        

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '*': return
        data = data.split(',')
        q = deque(data)

        node_q = deque()
        head = TreeNode(data[0])
        node_q.append(head)
        q.popleft()

        while node_q:
            node = node_q.popleft()

            left = q.popleft()
            right = q.popleft()

            if left != 'None':
                node.left = TreeNode(left)
                node_q.append(node.left)
            if right != 'None':
                node.right = TreeNode(right)
                node_q.append(node.right)

        return head
            


# Your Codec object will be instantiated and called as such:
ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
t = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(-1)), TreeNode(3, TreeNode(4))))
a = ser.deserialize(ser.serialize(t))
print(a)