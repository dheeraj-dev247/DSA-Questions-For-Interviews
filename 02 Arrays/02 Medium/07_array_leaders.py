"""
ARRAY LEADERS
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array arr[] of size n, an element is called
an Array Leader if it is greater than or equal to
every element on its right.

Return all leaders in their original left-to-right
order.

------------------------------------------------
EXAMPLES:
------------------------------------------------
Input:  [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]

Input:  [7, 10, 4, 10, 6, 5, 2]
Output: [10, 10, 6, 5, 2]

Input:  [1, 2, 3]
Output: [3]

------------------------------------------------
NAIVE IDEA (NOT OPTIMAL):
------------------------------------------------
- For each element, check all elements to its right.
- If none is greater, it is a leader.

Time Complexity: O(n²)
Not suitable for large arrays.

------------------------------------------------
OPTIMAL APPROACH (RIGHT-TO-LEFT SCAN)
------------------------------------------------
INTUITION:
------------------------------------------------
- Traverse the array from right to left.
- Keep track of the maximum element seen so far (maxi).
- If current element >= maxi, it is a leader.
- Update maxi whenever a new leader is found.
- Reverse the result at the end to restore left-to-right order.

------------------------------------------------
WHY THIS WORKS:
------------------------------------------------
- From the right, we already know all elements
  that lie to the right of the current index.
- Tracking a running maximum avoids repeated comparisons.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1) extra (output list excluded)

------------------------------------------------
CODE:
------------------------------------------------
"""


def find_array_leaders(arr):
    """
    Finds all leaders in the array using an optimal approach.
    """

    n = len(arr)
    maxi = float("-inf")  # Stores maximum element seen so far (from the right)
    result = []  # Stores leaders (right-to-left order initially)

    # Traverse array from right to left
    for i in range(n - 1, -1, -1):

        # If current element is greater than or equal to maxi
        if arr[i] >= maxi:
            result.append(arr[i])  # Current element is a leader
            maxi = arr[i]  # Update running maximum

    # Reverse result to restore left-to-right order
    result.reverse()

    return result


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    arr1 = [16, 17, 4, 3, 5, 2]
    arr2 = [7, 10, 4, 10, 6, 5, 2]
    arr3 = [1, 2, 3]

    print("Array:", arr1)
    print("Leaders:", find_array_leaders(arr1))

    print()

    print("Array:", arr2)
    print("Leaders:", find_array_leaders(arr2))

    print()

    print("Array:", arr3)
    print("Leaders:", find_array_leaders(arr3))
