from collections import deque


def maxSlidingWindow(nums, k):
    if not nums:
        return []
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove indices out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Append the maximum for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
