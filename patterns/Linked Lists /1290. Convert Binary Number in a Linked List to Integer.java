// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

// Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number. Return the decimal value of the number in the linked list. The most significant bit is at the head of the linked list.
// O(n) run time (n => number of nodes)
// O(n) space because making extra 

class Solution {

    public int getDecimalValue(ListNode head) {
        ListNode dummy = head;
        int counter = 0;
        while (dummy != null) {
            counter++;
            dummy = dummy.next;
        }
        dummy = head;
        int decValue = 0;
        for (int i = 0; i < counter; i++) {
            decValue += dummy.val * Math.pow(2, counter - 1 - i);
            dummy = dummy.next;
        }
        return decValue;
    }
}
