# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=problem-list-v2&envId=linked-list


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Create a dummy node to handle edge case where left = 1
        dummy = ListNode(0)
        dummy.next = head

        # Find the node just before the left position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Start of the portion to be reversed
        curr = prev.next

        # Reverse the portion from left to right
        for _ in range(right - left):
            # Store the next node
            next_node = curr.next
            # Update curr.next to skip next_node
            curr.next = next_node.next
            # Insert next_node between prev and curr
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
