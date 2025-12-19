"""
LINEAR SEARCH
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers and a target value,
find the index of the target element in the array.

If the element is not present, return -1.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Traverse the array from left to right.
- Compare each element with the target.
- If a match is found, return its index immediately.
- If traversal ends without a match, return -1.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Linear search does not require the array to be sorted.
- Every element is checked exactly once in the worst case.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(1) → target found at first position
- Average Case: O(n)
- Worst Case:   O(n) → target not found or at last position

Space Complexity:
- O(1) → constant extra space

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Works on both sorted and unsorted arrays.
- Very simple but inefficient for large datasets.
- Often used when array size is small.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → return -1
- Multiple occurrences → returns first occurrence
- Target not present in array

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def linear_search(arr, target):
    """
    Performs linear search to find the target element.

    Parameters:
    arr (list): List of integers
    target (int): Element to search for

    Returns:
    int: Index of target element if found, else -1
    """

    # Traverse through each element in the array
    for i in range(len(arr)):

        # Check if current element matches the target
        if arr[i] == target:
            return i  # Target found

    # Target not found
    return -1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [10, 23, 45, 70, 11, 15]
    target = 70

    print("Array:", data)
    print("Target:", target)

    # Perform linear search
    index = linear_search(data, target)

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")
