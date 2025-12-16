"""
INSERTION SORT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS INSERTION SORT?
------------------------------------------------
Insertion Sort is a simple and intuitive comparison-based
sorting algorithm.

It works the same way we sort playing cards in our hand:
- We take one element at a time
- Place it in its correct position among the already
  sorted elements

------------------------------------------------
HOW THE ALGORITHM WORKS (STEP-BY-STEP):
------------------------------------------------
1. Assume the first element is already sorted.
2. Pick the next element (called the key).
3. Compare the key with elements in the sorted part.
4. Shift all elements greater than the key one position
   to the right.
5. Insert the key at its correct position.
6. Repeat until the array is sorted.

------------------------------------------------
KEY IDEA:
------------------------------------------------
At every step, the left part of the array is always sorted,
and we insert the next element into this sorted part.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n)    → when the array is already sorted
- Average Case: O(n^2)
- Worst Case:   O(n^2)  → when the array is sorted in reverse order

Space Complexity:
- O(1) → In-place sorting algorithm

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Insertion Sort is a stable sorting algorithm.
- Very efficient for small datasets.
- Performs well on nearly sorted arrays.
- Used in practice inside more advanced algorithms.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array → already sorted
- Single element → already sorted
- Array with duplicate elements

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def insertion_sort(arr):
    """
    Sorts the given list in ascending order using Insertion Sort.

    Parameters:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list
    """

    # Traverse from the second element to the end
    for i in range(1, len(arr)):

        # Store the current element to be inserted
        key = arr[i]

        # Initialize pointer for the sorted part
        j = i - 1

        # Shift elements of the sorted part that are
        # greater than the key one position to the right
        while j >= 0 and arr[j] > key:

            # Move the larger element one step right
            arr[j + 1] = arr[j]

            # Move pointer to the left
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

    # Return the sorted array
    return arr


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [12, 11, 13, 5, 6]

    # Print original array
    print("Original array:", data)

    # Call insertion sort function
    sorted_data = insertion_sort(data)

    # Print sorted array
    print("Sorted array:", sorted_data)