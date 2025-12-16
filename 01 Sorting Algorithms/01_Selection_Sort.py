"""
SELECTION SORT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS SELECTION SORT?
------------------------------------------------
Selection Sort is a simple comparison-based sorting algorithm.
It works by repeatedly selecting the smallest element from the
unsorted portion of the array and placing it at the beginning.

The array is conceptually divided into two parts:
1. Sorted part (left side)
2. Unsorted part (right side)

Initially, the sorted part is empty, and the entire array
is unsorted.

------------------------------------------------
HOW THE ALGORITHM WORKS (STEP-BY-STEP):
------------------------------------------------
1. Start from index 0.
2. Find the minimum element from index 0 to n-1.
3. Swap the minimum element with the element at index 0.
4. Move to index 1.
5. Repeat the process until the array is sorted.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n^2)
- Average Case: O(n^2)
- Worst Case:   O(n^2)

Space Complexity:
- O(1) → In-place sorting algorithm (no extra memory used)

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Selection Sort is NOT stable.
- It always performs n(n-1)/2 comparisons.
- Useful for small datasets or when memory usage is critical.
- Not suitable for large datasets.

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


def selection_sort(arr):
    """
    Sorts the given list in ascending order using Selection Sort.

    Parameters:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list
    """

    # Store the length of the array
    n = len(arr)

    # Outer loop runs n - 1 times
    # Each iteration places one element at its correct position
    for i in range(n - 1):

        # Assume the current index holds the smallest element
        min_index = i

        # Inner loop to find the minimum element in unsorted part
        for j in range(i + 1, n):

            # If a smaller element is found, update min_index
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest found element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the sorted array
    return arr


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [64, 25, 12, 22, 11]

    # Print original array
    print("Original array:", data)

    # Call selection sort function
    sorted_data = selection_sort(data)

    # Print sorted array
    print("Sorted array:", sorted_data)
