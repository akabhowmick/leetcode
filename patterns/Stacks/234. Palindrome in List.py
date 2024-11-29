# https://leetcode.com/problems/palindrome-linked-list/?envType=problem-list-v2&envId=stack

# does not use the stacks too well

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next
#         while stack:
#             if len(stack) != 1:
#                 if stack[0] == stack[-1]:
#                     stack.pop(0)
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 return True
#         return len(stack) == 0


class Solution:
    def isPalindrome(self, head: ListNode) -> bool: # type: ignore
        if not head or not head.next:
            return True

        # Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Compare the two halves
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
