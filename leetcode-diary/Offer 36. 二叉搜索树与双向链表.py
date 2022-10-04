# Definition for a Node.
from pickle import NONE
from platform import node
from sre_constants import NOT_LITERAL_UNI_IGNORE
from tempfile import template


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 定义 left 为前，right 为后
        # 尝试使用递归完成，既然是顺序连接，那么根节点必定是中间的那一个
        if root == None:
            return None
        if root.left == root.right == None:
            root.left= root
            root.right = root
            return root
        head = root
        tempt_right, tempt_left = root.right, root.left
        if tempt_left:
            left_head = self.treeToDoublyList(tempt_left)
            # 将 root 和 left 连接为一个双循环链表
            head, last_of_left = left_head, left_head.left
            last_of_left.right, root.right = root, head
            root.left, head.left = last_of_left, root
        if tempt_right:
            right_head = self.treeToDoublyList(tempt_right)
            # 将 root 和 right 连接为一个双循环链表
            last_of_right = right_head.left
            root.right, last_of_right.right = right_head, head
            right_head.left, head.left = root, last_of_right
        return head

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            nonlocal pre, head
            if not cur: return
            dfs(cur.left) # 递归左子树
            if pre: # 修改节点引用
                pre.right, cur.left = cur, pre
            else: # 记录头节点
                head = cur
            pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        pre, head = None, None
        dfs(root)
        head.left, pre.right = pre, head
        return head

test = Solution()
root = Node(4, Node(2, Node(1), Node(3)), Node(5))
# root = Node(4, Node(2), Node(5))
root = Node(2, None, Node(3))
print(test.treeToDoublyList(root))
        