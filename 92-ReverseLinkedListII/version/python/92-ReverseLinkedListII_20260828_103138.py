# Last updated: 28/08/2026, 10:31:38
1class Solution(object):
2    def reverseBetween(self, head, left, right):
3        """
4        :type head: Optional[ListNode]
5        :type left: int
6        :type right: int
7        :rtype: Optional[ListNode]
8        """
9        if not head or left == right:
10            return head
11            
12        dummy = ListNode(0)
13        dummy.next = head
14        prev = dummy
15        
16        # 1. Move prev to the node just before the 'left' position
17        for _ in range(left - 1):
18            prev = prev.next
19            
20        # 2. Reverse the sublist from left to right
21        current = prev.next
22        for _ in range(right - left):
23            next_node = current.next
24            current.next = next_node.next
25            next_node.next = prev.next
26            prev.next = next_node
27            
28        return dummy.next