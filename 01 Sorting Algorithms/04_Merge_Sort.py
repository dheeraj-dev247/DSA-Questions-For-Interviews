"""
MERGE SORT ALGORITHM
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS MERGE SORT?
------------------------------------------------
Merge Sort is a classic Divide and Conquer
sorting algorithm.

It works in three major steps:
1. Divide  – Split the array into two halves
2. Conquer – Recursively sort each half
3. Combine – Merge the two sorted halves

Merge Sort guarantees O(n log n) time complexity
in best, average, and worst cases.

------------------------------------------------
WHY USE MERGE SORT?
------------------------------------------------
- Predictable performance
- Very efficient for large datasets
- Stable sorting algorithm
- Used internally in many systems

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:  [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

------------------------------------------------
APPROACH OVERVIEW:
------------------------------------------------
- Recursively divide the array until size = 1
- Merge subarrays in sorted order

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Space Complexity:
- O(n) (extra space for merging)

------------------------------------------------
CODE IMPLEMENTATION:
------------------------------------------------
"""


def merge_sort(arr, l, r):
    """
    Recursively divides the array and sorts it.
    """

    # Base condition: if subarray has one or zero elements
    if l < r:

        # Find the middle point
        mid = (l + r) // 2

        # Recursively sort the left half
        merge_sort(arr, l, mid)

        # Recursively sort the right half
        merge_sort(arr, mid + 1, r)

        # Merge the two sorted halves
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    """
    Merges two sorted subarrays:
    arr[l..mid] and arr[mid+1..r]
    """

    # Create temporary arrays
    left = arr[l : mid + 1]
    right = arr[mid + 1 : r + 1]

    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    k = l  # Pointer for main array

    # Merge left and right arrays
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements from left array (if any)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right array (if any)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


"""
------------------------------------------------
DRY RUN (SMALL EXAMPLE)
------------------------------------------------
Array: [34, 25, 11]

Split:
Left  = [34]
Right = [25, 11]

Sort Right:
Split [25, 11] → [25] and [11]
Merge → [11, 25]

Final Merge:
Merge [34] and [11, 25]
→ Compare 34 & 11 → take 11
→ Compare 34 & 25 → take 25
→ Take remaining 34

Result: [11, 25, 34]
------------------------------------------------
"""


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original Array:", arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted Array:", arr)
