"""
REMOVE DUPLICATES FROM SORTED ARRAY
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given a sorted array, remove the duplicate elements
such that each element appears only once.

The relative order of elements must be maintained.

Return the number of unique elements and modify
the array in-place.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Since the array is already sorted, all duplicates
  will be adjacent.
- Use two pointers:
  - One pointer (i) to track the position of unique elements.
  - Another pointer (j) to scan the array.
- When a new (different) element is found, place it
  at the next unique position.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Sorted property guarantees duplicates are consecutive.
- No extra space is needed (in-place update).

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n) → single traversal of the array

Space Complexity:
- O(1) → constant extra space

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Array must be sorted.
- In-place modification is required.
- Common LeetCode / interview problem.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → return 0
- Array with one element → return 1
- Array with all duplicate elements

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def remove_duplicates(arr):
    """
    Removes duplicates from a sorted array in-place.

    Parameters:
    arr (list): Sorted list of integers

    Returns:
    int: Number of unique elements
    """

    # If the array is empty, no unique elements
    if len(arr) == 0:
        return 0

    # Pointer for the position of next unique element
    i = 0

    # Traverse the array starting from the second element
    for j in range(1, len(arr)):

        # If current element is different from last unique element
        if arr[j] != arr[i]:

            # Move pointer forward
            i += 1

            # Place the unique element at index i
            arr[i] = arr[j]

    # Number of unique elements is i + 1
    return i + 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [1, 1, 2, 2, 3, 4, 4, 5]

    print("Original array:", data)

    # Remove duplicates
    k = remove_duplicates(data)

    # Print results
    print("Number of unique elements:", k)
    print("Array after removing duplicates:", data[:k])