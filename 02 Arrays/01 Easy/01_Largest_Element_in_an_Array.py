"""
FIND THE LARGEST ELEMENT IN AN ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers, find the largest (maximum)
element present in the array.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Traverse the array from left to right.
- Keep track of the maximum element seen so far.
- Update the maximum whenever a larger element is found.
- After traversing the entire array, the stored value
  will be the largest element.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Every element is compared once.
- By maintaining a running maximum, we ensure the
  largest element is never missed.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n) → where n is the number of elements in the array

Space Complexity:
- O(1) → constant extra space used

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- This is a basic array traversal problem.
- Often asked as a warm-up or screening question.
- Can be solved without sorting (sorting would be inefficient).

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → invalid input
- Single element → that element is the largest
- Array with negative numbers
- Array with duplicate maximum values

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def find_largest_element(arr):
    """
    Finds and returns the largest element in the array.

    Parameters:
    arr (list): List of integers

    Returns:
    int: Largest element in the array
    """

    # Check if the array is empty
    if len(arr) == 0:
        raise ValueError("Array is empty")

    # Assume the first element is the largest initially
    largest = arr[0]

    # Traverse the array starting from the second element
    for i in range(1, len(arr)):

        # If current element is greater than the stored largest
        if arr[i] > largest:

            # Update the largest value
            largest = arr[i]

    # Return the largest element
    return largest


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [10, 5, 20, 8, 25, 3]

    # Print the array
    print("Array:", data)

    # Find the largest element
    result = find_largest_element(data)

    # Print the result
    print("Largest element:", result)
