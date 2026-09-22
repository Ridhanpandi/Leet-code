# Last updated: 22/09/2026, 10:11:51
1class Solution:
2    def hasCycle(self, head: Optional[ListNode]) -> bool:
3    
4        fast = head
5        slow = head
6        
7        while fast and fast.next:
8            fast = fast.next.next
9            slow = slow.next
10            
11            if fast == slow:
12                return True
13    
14        return False