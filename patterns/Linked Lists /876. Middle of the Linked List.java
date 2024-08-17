// https://leetcode.com/problems/middle-of-the-linked-list/

// Tags: Linked List, Two Pointers 
// Description:
// Given the head of a singly linked list, return the middle node of the linked list.
// If there are two middle nodes, return the second middle node.

class Solution {
  public ListNode middleNode(ListNode head) {
      ListNode fast = head; 
      ListNode slow = head; 
      int size = 0; 
      while(fast!=null){
          fast = fast.next; 
          size++; 
      }
      size = size/2; 
      while(size > 0){
          slow = slow.next; 
          size--; 
      }
      return slow; 
  }
}