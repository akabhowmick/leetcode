/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// https://leetcode.com/problems/reverse-nodes-in-k-group/
// Description: Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

//  O(n) time complexity 
//  O(1) space complexity 

// Approach: 
// 1. Edge Case of if k == 1 
// 2. Calculate the number of nodes => helps to know how many groups needed
// 3. Reverse Nodes in Groups of k
//  a. Main hard part => uses a nested while loop 
// 4. Connect the Remaining Nodes (if any)
// 5. Return the modified list

class Solution {
  public ListNode reverseKGroup(ListNode head, int k) {
    // the swaps are happening every node so no swap
    if(k==1)
    return head 
    ListNode temp=head;
    ListNode prev=null;
    ListNode next=head.next;
    ListNode first=null;
    ListNode nhead=null;
    // calculate the length using a while loop
    int len = 0; 
    while(temp != null){
    temp = temp.next
        len++; 
    }

    // reset temp 
    temp = head;
      
    // number of k groups
    int cnt=len/k;
    while(cnt>0){
        int t=k;
        if(first==null)
        first=temp;
        ListNode end=temp;
        while(t>0){
            temp.next=prev;
            prev=temp;
            temp=next;
            if(next!=null)
            next=next.next;
            --t;
        }
        if(nhead==null){
            nhead=prev;
        }
        else{
            first.next=prev;
            first=end;
        }
        --cnt;
        prev=null;
    }
    first.next=temp;
    return nhead;
    }
}