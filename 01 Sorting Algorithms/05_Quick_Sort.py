"""
QUICK SORT (FIRST ELEMENT AS PIVOT) - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS QUICK SORT?
------------------------------------------------
Quick Sort is a divide-and-conquer based sorting algorithm.

The main idea is:
- Pick a pivot element
- Place the pivot at its correct position
- Place all smaller elements to the left of the pivot
- Place all larger elements to the right of the pivot
- Recursively apply the same process on left and right subarrays

------------------------------------------------
PIVOT SELECTION (FIRST ELEMENT):
------------------------------------------------
In this implementation:
- The first element of the array is chosen as the pivot.
- This is easy to understand and commonly asked in interviews.

⚠️ NOTE:
- This pivot choice gives worst-case O(n^2) for already
  sorted or reverse sorted arrays.

------------------------------------------------
DIVIDE AND CONQUER STRATEGY:
------------------------------------------------
1. Divide:
   - Partition the array around the pivot.

2. Conquer:
   - Recursively sort left and right subarrays.

3. Combine:
   - No merging needed (in-place sorting).

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n^2)

Space Complexity:
- O(log n) average (recursion stack)
- O(n) worst case

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Quick Sort is NOT stable.
- In-place sorting algorithm.
- Faster than Merge Sort in practice.
- Pivot selection greatly affects performance.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → already sorted
- Single element → already sorted
- Duplicate elements allowed

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def quick_sort(arr, low, high):
    """
    Sorts the array in ascending order using Quick Sort
    with the FIRST element as pivot.

    Parameters:
    arr (list): List of integers
    low (int): Starting index
    high (int): Ending index
    """

    # Base condition
    if low < high:

        # Partition the array and get pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort left subarray
        quick_sort(arr, low, pivot_index - 1)

        # Recursively sort right subarray
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    Partitions the array using the FIRST element as pivot.

    Parameters:
    arr (list): List of integers
    low (int): Starting index (pivot position)
    high (int): Ending index

    Returns:
    int: Final position of the pivot
    """

    # Choose the first element as pivot
    pivot = arr[low]

    # Initialize pointers
    i = low + 1  # Left pointer
    j = high  # Right pointer

    # Loop until pointers cross
    while True:

        # Move i to the right while elements are <= pivot
        while i <= j and arr[i] <= pivot:
            i += 1

        # Move j to the left while elements are > pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # If pointers cross, stop
        if i > j:
            break

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at its correct position
    arr[low], arr[j] = arr[j], arr[low]

    # Return pivot index
    return j


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [10, 7, 8, 9, 1, 5]

    # Print original array
    print("Original array:", data)

    # Call quick sort
    quick_sort(data, 0, len(data) - 1)

    # Print sorted array
    print("Sorted array:", data)
