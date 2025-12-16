"""
BUBBLE SORT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS BUBBLE SORT?
------------------------------------------------
Bubble Sort is a simple comparison-based sorting algorithm.
It works by repeatedly swapping adjacent elements if they
are in the wrong order.

The algorithm gets its name because larger elements
"bubble up" to the end of the array after each pass.

------------------------------------------------
HOW THE ALGORITHM WORKS (STEP-BY-STEP):
------------------------------------------------
1. Start from the beginning of the array.
2. Compare adjacent elements.
3. If the current element is greater than the next one,
   swap them.
4. Continue this process for the entire array.
5. After each pass, the largest element is placed at
   the end of the array.
6. Repeat the process for the remaining unsorted portion
   until the array is sorted.

------------------------------------------------
OPTIMIZATION (IMPORTANT):
------------------------------------------------
If during a full pass no swaps are made, the array is
already sorted. In this case, we can stop early.

This optimization improves performance for nearly
sorted arrays.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n)  → when the array is already sorted (with optimization)
- Average Case: O(n^2)
- Worst Case:   O(n^2)

Space Complexity:
- O(1) → In-place sorting algorithm

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Bubble Sort is a stable sorting algorithm.
- Very easy to understand and implement.
- Inefficient for large datasets.
- Mainly used for educational purposes.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → already sorted
- Single element → already sorted
- Array with duplicate values

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def bubble_sort(arr):
    """
    Sorts the given list in ascending order using Bubble Sort.

    Parameters:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list
    """

    # Store the length of the array
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):

        # Flag to check if any swapping happened in this pass
        swapped = False

        # Last i elements are already sorted, so we ignore them
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:

                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Mark that a swap has occurred
                swapped = True

        # If no swaps happened, the array is already sorted
        if not swapped:
            break

    # Return the sorted array
    return arr


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [64, 34, 25, 12, 22, 11, 90]

    # Print original array
    print("Original array:", data)

    # Call bubble sort function
    sorted_data = bubble_sort(data)

    # Print sorted array
    print("Sorted array:", sorted_data)
