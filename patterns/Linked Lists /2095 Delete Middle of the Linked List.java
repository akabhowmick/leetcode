// You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

// Tags: Linked List Two Pointers
// Time Complexity: The algorithm runs in O(n) time, where n is the number of nodes in the linked list, because it traverses the list only once.
class Solution {

    public ListNode deleteMiddle(ListNode head) {
        // Edge case: if there's only one node, return null
        if (head == null || head.next == null) {
            return null;
        }

        // Initialize two pointers
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null; // Keep track of the node before slow

        // Use fast and slow to find the middle node
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            prev = slow;       // Update the previous node
            slow = slow.next;  // Move slow one step
        }

        // Delete the middle node by skipping it
        if (prev != null) {
            prev.next = slow.next;
        }

        return head; // Return the head of the modified list
    }
}
