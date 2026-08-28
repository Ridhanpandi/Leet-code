# Last updated: 28/08/2026, 10:37:30
1class Solution(object):
2    def deleteDuplicates(self, head):
3        """
4        :type head: Optional[ListNode]
5        :rtype: Optional[ListNode]
6        """
7        current = head
8        
9        while current and current.next:
10            if current.val == current.next.val:
11                current.next = current.next.next
12            else:
13                current = current.next
14                
15        return head