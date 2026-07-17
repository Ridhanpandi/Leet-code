// Last updated: 17/07/2026, 14:45:52
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode rotateRight(ListNode head, int k) {
13        if (head == null || head.next == null || k == 0) {
14            return head;
15        }
16
17        // Step 1: find length and tail
18        int n = 1;
19        ListNode tail = head;
20        while (tail.next != null) {
21            tail = tail.next;
22            n++;
23        }
24
25        // Step 2: reduce k
26        k = k % n;
27        if (k == 0) {
28            return head;
29        }
30
31        // Step 3: make circular
32        tail.next = head;
33
34        // Step 4: find new tail
35        int steps = n - k;
36        ListNode newTail = head;
37        for (int i = 1; i < steps; i++) {
38            newTail = newTail.next;
39        }
40
41        // Step 5: break
42        ListNode newHead = newTail.next;
43        newTail.next = null;
44
45        return newHead;
46    }
47}