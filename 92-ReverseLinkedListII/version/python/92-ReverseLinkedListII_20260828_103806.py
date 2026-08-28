# Last updated: 28/08/2026, 10:38:06
1class Solution(object):
2    def deleteDuplicates(self, head):
3        """
4        :type head: Optional[ListNode]
5        :rtype: Optional[ListNode]
6        """
7        dummy = ListNode(0, head)
8        prev = dummy
9        
10        while head:
11            # If it's a start of duplicates sub-list
12            if head.next and head.val == head.next.val:
13                # Move head until the end of duplicates
14                while head.next and head.val == head.next.val:
15                    head = head.next
16                # Skip all duplicates
17                prev.next = head.next
18            else:
19                prev = prev.next
20                
21            head = head.next
22            
23        return dummy.next