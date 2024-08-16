// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// The solution is to use two pointers, fast and slow. fast will get a head start of n nodes, and then we'll move up both pointers until fast reaches the end of the list. Then at that point, slow will be perfectly positioned n nodes behind fast, and we can use slow to make node n-1 skip node n (please see the video for a visualization of this).

// In the worst case, each pointer will traverse the entire list once, so this runs in O(n) time. We will also only ever need 2 extra pointers, so this also runs in O(1) space.

// Linked Lists 


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        