"""
CHECK IF THE ARRAY IS SORTED (NON-DECREASING ORDER)
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers, check whether the array
is sorted in non-decreasing (ascending) order.

Return True if the array is sorted, otherwise False.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Traverse the array from left to right.
- Compare every element with its next element.
- If at any point the current element is greater
  than the next one, the array is NOT sorted.
- If no such case is found, the array is sorted.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- A sorted array must satisfy:
  arr[i] <= arr[i + 1] for all valid i.
- Only one violation is enough to conclude it is not sorted.

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
- Clarify whether sorting means strictly increasing
  or non-decreasing (duplicates allowed).
- This solution checks for NON-DECREASING order.
- Very common warm-up interview question.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → sorted
- Single element → sorted
- Array with duplicate values → still sorted

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def is_array_sorted(arr):
    """
    Checks if the given array is sorted in non-decreasing order.

    Parameters:
    arr (list): List of integers

    Returns:
    bool: True if array is sorted, False otherwise
    """

    # Traverse the array and compare adjacent elements
    for i in range(len(arr) - 1):

        # If current element is greater than next element
        if arr[i] > arr[i + 1]:

            # Array is not sorted
            return False

    # If no violations found, array is sorted
    return True


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Test case 1: Sorted array
    arr1 = [1, 2, 2, 3, 4, 5]
    print("Array:", arr1)
    print("Is sorted?", is_array_sorted(arr1))

    print()

    # Test case 2: Unsorted array
    arr2 = [3, 1, 4, 2]
    print("Array:", arr2)
    print("Is sorted?", is_array_sorted(arr2))

    print()

    # Test case 3: Single element
    arr3 = [10]
    print("Array:", arr3)
    print("Is sorted?", is_array_sorted(arr3))