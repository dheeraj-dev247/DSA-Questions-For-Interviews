"""
SECOND LARGEST & SECOND SMALLEST ELEMENTS IN AN ARRAY
DETAILED NOTES + CODE (PYTHON)

====================================================
PROBLEM 1:
----------------------------------------------------
Find the SECOND LARGEST element in an array
WITHOUT SORTING.

----------------------------------------------------
PROBLEM 2:
----------------------------------------------------
You are given an array 'a' of 'n' UNIQUE non-negative
integers.

Find:
- Second Largest element
- Second Smallest element

Return both as an array of size 2:
[second_largest, second_smallest]

====================================================
WHY NOT SORT?
----------------------------------------------------
- Sorting takes O(n log n) time.
- Both problems can be solved in O(n) time
  using a single traversal.

====================================================
TIME AND SPACE COMPLEXITY:
----------------------------------------------------
Time Complexity:
- O(n) for both problems

Space Complexity:
- O(1) extra space

====================================================
IMPORTANT INTERVIEW NOTES:
----------------------------------------------------
- Elements are UNIQUE in Problem 2 → no duplicates.
- Must carefully update largest, second largest,
  smallest, and second smallest.
- Very commonly asked array problem.

====================================================
EDGE CASES:
----------------------------------------------------
- Array size < 2 → invalid
- Exactly 2 elements → directly answer
- All values are non-negative integers

====================================================
IMPLEMENTATION BELOW:
====================================================
"""


def find_second_largest(arr):
    """
    PROBLEM 1:
    Finds the second largest element in the array
    without sorting.

    Parameters:
    arr (list): List of integers

    Returns:
    int: Second largest element
    """

    # Array must have at least two elements
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")

    # Initialize largest and second largest
    largest = float("-inf")
    second_largest = float("-inf")

    # Traverse the array
    for num in arr:

        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num

        # Update second largest only if num is smaller than largest
        elif num > second_largest and num != largest:
            second_largest = num

    # If second largest was never updated
    if second_largest == float("-inf"):
        raise ValueError("No second largest element exists")

    return second_largest


def find_second_largest_and_second_smallest(arr):
    """
    PROBLEM 2:
    Finds the second largest and second smallest elements
    in an array of UNIQUE non-negative integers.

    Parameters:
    arr (list): List of unique non-negative integers

    Returns:
    list: [second_largest, second_smallest]
    """

    # Array must have at least two elements
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")

    # Initialize smallest and second smallest
    smallest = float("inf")
    second_smallest = float("inf")

    # Initialize largest and second largest
    largest = float("-inf")
    second_largest = float("-inf")

    # Single traversal of the array
    for num in arr:

        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    # Return result as per problem statement
    return [second_largest, second_smallest]


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # -------- Problem 1 Test --------
    data1 = [12, 35, 1, 10, 34, 1]
    print("Array:", data1)
    print("Second largest element:", find_second_largest(data1))

    print()

    # -------- Problem 2 Test --------
    data2 = [5, 7, 2, 9, 1, 6]
    print("Array:", data2)
    print(
        "Second largest & second smallest:",
        find_second_largest_and_second_smallest(data2),
    )
