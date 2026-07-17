# Last updated: 17/07/2026, 14:40:41
1class Solution:
2    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        dummy = ListNode(0, head)
4        prev = dummy
5
6        while prev.next and prev.next.next:
7            first = prev.next
8            second = first.next
9
10            first.next = second.next
11            second.next = first
12            prev.next = second
13
14            prev = first
15
16        return dummy.next