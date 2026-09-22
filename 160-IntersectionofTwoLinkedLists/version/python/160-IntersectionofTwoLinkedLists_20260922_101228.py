# Last updated: 22/09/2026, 10:12:28
1class Solution:
2    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
3        lista = headA
4        listb = headB
5
6        while lista != listb:
7            lista = lista.next if lista else headB
8            listb = listb.next if listb else headA
9        
10        return listb