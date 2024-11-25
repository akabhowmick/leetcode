# Concept of a Monotonic Increasing Stack
# Maintain increasing order: The stack should ensure that the top of the stack always has the largest (or equal) value.
# Pop elements if needed: If a new element is smaller than the top, pop elements until the new element can be added without violating the increasing order.
# Use case: Monotonic stacks are helpful for problems like finding the Next Greater Element, temperature analysis, and sliding window problems.


def monotonic_increasing_stack(nums):
    # Initialize the stack
    stack = []

    # Iterate through each number in the list
    for num in nums:
        # Maintain the monotonic property: pop elements from the stack
        # if they are greater than the current number (num)
        while stack and stack[-1] > num:
            stack.pop()

        # Add the current number to the stack
        stack.append(num)

        # Output the current state of the stack for debugging
        print(f"After adding {num}: {stack}")

    return stack


def monotonic_increasing_stack(nums):
    # Initialize the stack
    stack = []

    # Iterate through each number in the list
    for num in nums:
        # Maintain the monotonic property: pop elements from the stack
        # if they are greater than the current number (num)
        while stack and stack[-1] > num:
            stack.pop()

        # Add the current number to the stack
        stack.append(num)

        # Output the current state of the stack for debugging
        print(f"After adding {num}: {stack}")

    return stack

nums = [5, 3, 8, 2, 10, 6]
result = monotonic_increasing_stack(nums)
print(f"Final Monotonic Increasing Stack: {result}")


# Usage Notes
# Adding Elements: If the new element is greater than or equal to the top of the stack, just push it onto the stack.
# Removing Elements: If the new element is smaller than the top of the stack, keep popping elements until you maintain the increasing order.
# Time Complexity:
# O(n) for the entire process since each element is pushed and popped at most once.
# Space complexity is O(n) for storing the stack.