#  https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-28

#  Description: Given the root of a binary tree, return the postorder traversal of its nodes' values.

#  Tags: Stack Trees DFS Binary Tree

# Time complexity O(n)


from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        num = []

        def f(root):
            if root == None:
                return num
            f(root.left)
            f(root.right)
            num.append(root.val)
            return num

        return f(root)


# class Solution {
#     public List<Integer> postorderTraversal(TreeNode root) {
#         List<Integer> result = new ArrayList<>();
#         fun(root,result);
#         return result;

#     }

#     private void fun(TreeNode root, List<Integer> result){
#         if(root != null){
#             fun(root.left,result);
#             fun(root.right,result);
#             result.add(root.val);
#         }
#     }

# }


# The approach used in the code is a simple recursive method to traverse the tree in postorder. The main method postorderTraversal initializes a list to store the result and then calls a helper function fun to perform the actual traversal.

# The 'fun' method is designed to:

# Traverse the left subtree by recursively calling itself on root.left.
# Traverse the right subtree by recursively calling itself on root.right.
# Process the current node by adding its value to the result list.