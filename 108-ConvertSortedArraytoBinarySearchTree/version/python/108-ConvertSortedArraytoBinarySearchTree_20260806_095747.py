# Last updated: 06/08/2026, 09:57:47
1class Solution(object):
2    def sortedArrayToBST(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: Optional[TreeNode]
6        """
7        def helper(left, right):
8            if left > right:
9                return None
10            
11            # Find the middle index
12            mid = (left + right) // 2
13            
14            # Create the root node with the middle element
15            root = TreeNode(nums[mid])
16            
17            # Recursively build the left and right subtrees
18            root.left = helper(left, mid - 1)
19            root.right = helper(mid + 1, right)
20            
21            return root
22            
23        return helper(0, len(nums) - 1)
24        