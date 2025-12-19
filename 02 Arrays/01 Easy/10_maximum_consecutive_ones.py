"""
MAXIMUM CONSECUTIVE ONES
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given a binary array (containing only 0s and 1s),
find the maximum number of consecutive 1s in the array.

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:  arr = [1, 1, 0, 1, 1, 1]
Output: 3

Explanation:
The longest continuous sequence of 1s is [1,1,1].

------------------------------------------------
APPROACH (LINEAR SCAN):
------------------------------------------------
- Traverse the array once.
- Maintain a counter for current consecutive 1s.
- Whenever a 1 is found, increment the counter.
- Whenever a 0 is found, reset the counter to 0.
- Keep track of the maximum value of the counter.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Consecutive means elements must be adjacent.
- A 0 breaks the sequence of 1s.
- Single pass is sufficient to track all sequences.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n)

Space Complexity:
- O(1)

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Very common array warm-up problem.
- Works only for binary arrays (0s and 1s).
- Simple but tests clarity of iteration logic.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Array with all 1s
- Array with all 0s
- Empty array
- Single element array

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def maximum_consecutive_ones(arr):
    """
    Finds the maximum number of consecutive 1s in a binary array.

    Parameters:
    arr (list): List containing only 0s and 1s

    Returns:
    int: Maximum count of consecutive 1s
    """

    max_count = 0  # Stores maximum consecutive 1s found
    current_count = 0  # Stores current consecutive 1s count

    # Traverse the array
    for num in arr:

        # If current element is 1, increase current count
        if num == 1:
            current_count += 1

            # Update maximum count if needed
            max_count = max(max_count, current_count)

        # If current element is 0, reset current count
        else:
            current_count = 0

    return max_count


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    arr = [1, 1, 0, 1, 1, 1]

    print("Array:", arr)

    # Find maximum consecutive ones
    result = maximum_consecutive_ones(arr)

    print("Maximum consecutive ones:", result)
