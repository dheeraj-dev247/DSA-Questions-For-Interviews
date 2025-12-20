"""
MAXIMUM SUBARRAY SUM
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an integer array nums, find the contiguous
subarray (containing at least one number) which
has the largest sum and return its sum.

------------------------------------------------
COMMON EXAMPLE (USED IN ALL APPROACHES):
------------------------------------------------
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

The maximum subarray is:
[4, -1, 2, 1]

Maximum Sum = 6

------------------------------------------------
APPROACH 1: BRUTE FORCE (TRIPLE LOOP)
------------------------------------------------
INTUITION:
------------------------------------------------
- Try every possible subarray.
- For each start index i and end index j,
  compute the sum using a third loop.
- Keep track of the maximum sum found.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n³)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def max_subarray_bruteforce(nums):
    """
    Brute force approach using three loops.
    """

    maxi = float("-inf")  # Stores the maximum subarray sum
    n = len(nums)

    # Pick starting index
    for i in range(n):

        # Pick ending index
        for j in range(i, n):

            cur_sum = 0

            # Sum elements from i to j
            for k in range(i, j + 1):
                cur_sum += nums[k]

            # Update maximum sum
            maxi = max(maxi, cur_sum)

    return maxi


"""
------------------------------------------------
APPROACH 2: BETTER BRUTE FORCE (DOUBLE LOOP)
------------------------------------------------
INTUITION:
------------------------------------------------
- Avoid recomputing the sum from scratch.
- Fix a start index i.
- Extend the subarray to the right using a
  running sum.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n²)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def max_subarray_better(nums):
    """
    Better brute force approach using two loops.
    """

    maxi = float("-inf")
    n = len(nums)

    # Pick starting index
    for i in range(n):

        running_sum = 0

        # Extend subarray to the right
        for j in range(i, n):
            running_sum += nums[j]
            maxi = max(maxi, running_sum)

    return maxi


"""
------------------------------------------------
APPROACH 3: OPTIMAL (KADANE'S ALGORITHM)
------------------------------------------------
CORE INSIGHT:
------------------------------------------------
- Keep a running sum of the current subarray.
- If the running sum becomes negative, drop it.
- A negative prefix can never help future sums.

------------------------------------------------
ALGORITHM STEPS:
------------------------------------------------
1. Initialize cur_sum = 0 and max_sum = -∞
2. Traverse the array:
   - Add current element to cur_sum
   - Update max_sum
   - If cur_sum < 0, reset it to 0

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def max_subarray_kadane(nums):
    """
    Optimal solution using Kadane's Algorithm.
    """

    max_sum = float("-inf")  # Best subarray sum found
    cur_sum = 0  # Current running sum

    # Traverse array
    for num in nums:

        # Extend current subarray
        cur_sum += num

        # Update maximum sum
        max_sum = max(max_sum, cur_sum)

        # If current sum becomes negative, reset it
        if cur_sum < 0:
            cur_sum = 0

    return max_sum


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Array:", nums)

    print("Brute Force Result:", max_subarray_bruteforce(nums))

    print("Better Brute Force Result:", max_subarray_better(nums))

    print("Optimal (Kadane) Result:", max_subarray_kadane(nums))
