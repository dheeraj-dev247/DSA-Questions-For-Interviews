"""
REARRANGE ARRAY ELEMENTS BY SIGN (LEETCODE 2149)
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an array of integers nums.

Rearrange the array so that:
- Positive and negative numbers appear alternately
- The arrangement starts with a positive number
- The number of positive and negative numbers is equal

------------------------------------------------
EXAMPLES:
------------------------------------------------
Input:  nums = [3, 1, -2, -5, 2, -4]
Output: [3, -2, 1, -5, 2, -4]

Input:  nums = [-1, 1]
Output: [1, -1]

------------------------------------------------
CONSTRAINTS:
------------------------------------------------
- Equal number of positive and negative elements
- Order among positives and negatives should be preserved

------------------------------------------------
APPROACH 1: BRUTE FORCE (TWO LISTS)
------------------------------------------------
INTUITION:
------------------------------------------------
1. Separate all positive and negative numbers
   into two different lists.
2. Place them back alternately:
   - Positive at even index
   - Negative at odd index

------------------------------------------------
WHY THIS WORKS:
------------------------------------------------
- Since counts are equal, we never run out
  of either positives or negatives.
- Simple and easy to understand.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)

------------------------------------------------
CODE:
------------------------------------------------
"""


def rearrange_bruteforce(nums):
    """
    Rearranges array by separating positives and negatives.
    """

    pos = []  # Store positive numbers
    neg = []  # Store negative numbers

    # Separate positives and negatives
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    # Rearrange alternately
    for i in range(len(pos)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]

    return nums


"""
------------------------------------------------
APPROACH 2: OPTIMAL (DIRECT PLACEMENT)
------------------------------------------------
INTUITION:
------------------------------------------------
- Instead of two lists, directly place elements
  into their correct positions in a new array.
- Use two pointers:
  - posIndex for positives (0, 2, 4, ...)
  - negIndex for negatives (1, 3, 5, ...)

------------------------------------------------
WHY THIS WORKS:
------------------------------------------------
- Equal number of positives and negatives
- Each number goes directly to its correct slot
- Single pass solution

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)

------------------------------------------------
CODE:
------------------------------------------------
"""


def rearrange_optimal(nums):
    """
    Rearranges array using optimal one-pass approach.
    """

    n = len(nums)
    ans = [0] * n  # Result array

    posIndex = 0  # Even index for positives
    negIndex = 1  # Odd index for negatives

    # Traverse the original array
    for num in nums:

        # Place negative numbers at odd indices
        if num < 0:
            ans[negIndex] = num
            negIndex += 2

        # Place positive numbers at even indices
        else:
            ans[posIndex] = num
            posIndex += 2

    return ans


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [3, 1, -2, -5, 2, -4]

    print("Original Array:", nums)

    print("Brute Force Result:", rearrange_bruteforce(nums.copy()))

    print("Optimal Result:", rearrange_optimal(nums))
