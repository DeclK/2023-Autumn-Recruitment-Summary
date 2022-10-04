# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack = [root]
        ret = []
        while stack:
            new_stack = []
            level_ret = [node.val for node in stack]
            ret.append(level_ret)
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return ret
        

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 使用队列的写法
        if root == None: return []
        stack = [root]
        ret = []
        while stack:
            level_ret = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level_ret.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            ret.append(level_ret)
        return ret
                

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 不过是层序遍历加上奇偶层判断罢了
        if root == None: return []
        stack = [root]
        ret = []
        level = 0
        while stack:
            level_ret = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level_ret.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            # if level:
            #     ret.append(level_ret[::-1])
            #     level = 0
            # else:
            #     ret.append(level_ret)
            #     level = 1
            ret.append(level_ret[::-1] if len(ret) % 2 else level_ret)
        return ret