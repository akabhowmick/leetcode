// https://leetcode.com/problems/add-two-numbers/description/
// Difficulty: Medium

// Problem
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
 */
// Solution, O(n) time and O(1) space
/*
Iterate over both linked lists, adding the results. If we get a carry, store that. On the next iteration, make sure to use that carry, then reset it before adding again. If we run out of a linked list, just keep adding the remaining linked list. If we end with a carry such as [9] + [9] then we need to add one more node to the end. I used a dummy node because it made more sense with the creation of the result nodes. For instance if we initialize a result node without a dummy, when we add two numbers we can populate the value, but if we create a new node for the next numbers to be added, we also have to check to make sure we have more numbers to add. Whereas the dummy node is offset by one, so every time we add, we create a node and append it to the dummy. We could also not use a dummy, but create the head of the linked list for the first time we add, though the code is more annoying to implement.
 */
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
class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0); // holds the resulting linked list
        ListNode tail = dummyHead; // keeps track of the last node in the result list 
        int carry = 0; // in case sum exceeds 10 
        while (l1 != null || l2 != null || carry != 0) {
            int l1Value = (l1 != null) ? l1.val : 0;
            int l2Value = (l2 != null) ? l2.val : 0;
            int sum = l1Value + l2Value + carry;
            int digit = sum % 10; // only wants the one ones place 
            carry = sum / 10;

            // add the new node 
            ListNode newNode = new ListNode(digit);
            tail.next = newNode;
            tail = tail.next;

            l1 = (l1 != null) ? l1.next : null; // update l1
            l2 = (l2 != null) ? l2.next : null; // update l2 
        }
        ListNode result = dummyHead.next;
        dummyHead.next = null;
        return result;
    }
}
