// O(n) run time 
// O(1) space 
// https://leetcode.com/problems/reverse-linked-list/
// Description: Given the head of a singly linked list, reverse the list, and return the reversed list.

// Tags: Linked List Recursion 


class Solution {
  public ListNode reverseList(ListNode head) {
      
      ListNode prev = null;
      ListNode next = null;
      ListNode curr = head;

      while(curr != null)
      {
          next = curr.next;

          curr.next = prev;

          prev = curr;
          curr = next;
      }

      return prev;
  }
}