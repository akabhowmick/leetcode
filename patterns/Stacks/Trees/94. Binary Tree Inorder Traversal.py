# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=stack


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
