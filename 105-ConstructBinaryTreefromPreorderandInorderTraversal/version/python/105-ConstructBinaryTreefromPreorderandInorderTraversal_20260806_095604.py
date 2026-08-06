# Last updated: 06/08/2026, 09:56:04
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution(object):
9    def buildTree(self, preorder, inorder):
10        """
11        :type preorder: List[int]
12        :type inorder: List[int]
13        :rtype: Optional[TreeNode]
14        """
15        # Map values to their indices in the inorder array for O(1) lookups
16        inorder_map = {val: i for i, val in enumerate(inorder)}
17        
18        self.pre_idx = 0
19        
20        def helper(left, right):
21            # If there is no element to construct the subtree
22            if left > right:
23                return None
24            
25            # Select the current root value from preorder using self.pre_idx
26            root_val = preorder[self.pre_idx]
27            self.pre_idx += 1
28            root = TreeNode(root_val)
29            
30            # Split inorder traversal into left and right subtrees
31            index = inorder_map[root_val]
32            
33            # Recursively build the left and right subtrees
34            root.left = helper(left, index - 1)
35            root.right = helper(index + 1, right)
36            
37            return root
38            
39        return helper(0, len(inorder) - 1)