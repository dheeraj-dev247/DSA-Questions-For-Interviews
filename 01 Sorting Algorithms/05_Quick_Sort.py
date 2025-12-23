"""
QUICK SORT ALGORITHM
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS QUICK SORT?
------------------------------------------------
Quick Sort is a Divide and Conquer sorting algorithm.

Main steps:
1. Choose a Pivot element
2. Partition the array around the pivot
3. Recursively apply Quick Sort to left and right subarrays

Quick Sort is usually very fast in practice due to
good cache performance, but it has a worst-case
time complexity of O(n²) if pivot selection is poor.

------------------------------------------------
WHY USE QUICK SORT?
------------------------------------------------
- Very fast in average cases
- In-place sorting (no extra arrays)
- Widely used in real-world libraries

------------------------------------------------
PIVOT STRATEGY USED HERE:
------------------------------------------------
- The FIRST element of the array segment is chosen
  as the pivot.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n²)

Space Complexity:
- Average: O(log n) due to recursion stack
- Worst:   O(n)

------------------------------------------------
CODE IMPLEMENTATION:
------------------------------------------------
"""


def partition(arr, low, high):
    """
    Partitions the array using the first element as pivot.

    After partition:
    - Elements <= pivot are on the left
    - Elements > pivot are on the right
    """

    pivot = arr[low]  # Choose first element as pivot
    i = low  # Pointer starting from left
    j = high  # Pointer starting from right

    # Continue until pointers cross
    while i < j:

        # Move i right while elements are <= pivot
        while i <= high - 1 and arr[i] <= pivot:
            i += 1

        # Move j left while elements are > pivot
        while j >= low + 1 and arr[j] > pivot:
            j -= 1

        # Swap if pointers haven't crossed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at its correct position
    arr[low], arr[j] = arr[j], arr[low]

    # Return pivot index
    return j


def quick_sort(arr, low, high):
    """
    Recursively sorts the array using Quick Sort.
    """

    # Base condition: at least two elements
    if low < high:

        # Partition the array
        p_index = partition(arr, low, high)

        # Sort elements before pivot
        quick_sort(arr, low, p_index - 1)

        # Sort elements after pivot
        quick_sort(arr, p_index + 1, high)


"""
------------------------------------------------
DRY RUN (SMALL EXAMPLE)
------------------------------------------------
Array: [34, 25, 11]

Pivot = 34
Partition:
- Left: [25, 11]
- Right: []

Recursive calls:
quick_sort([25, 11])
→ Pivot = 25
→ Merge → [11, 25]

Final merge:
[11, 25, 34]
------------------------------------------------
"""


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]

    print("Original Array:", arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("Sorted Array:", arr)
