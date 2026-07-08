// Last updated: 08/07/2026, 20:50:04
class Solution {
    public ListNode sortList(ListNode head) {
        // Base case
        if (head == null || head.next == null) return head;

        // Step 1: Find middle and split
        ListNode mid = getMid(head);
        ListNode right = mid.next;
        mid.next = null;

        // Step 2: Recursively sort both halves
        ListNode left = sortList(head);
        right = sortList(right);

        // Step 3: Merge in ASCENDING order
        return merge(left, right);
    }

    ListNode getMid(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {  // <= ensures ASCENDING order
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        if (l1 != null) curr.next = l1;
        if (l2 != null) curr.next = l2;
        return dummy.next;
    }
}