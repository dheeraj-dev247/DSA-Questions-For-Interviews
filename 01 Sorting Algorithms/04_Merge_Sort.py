"""
MERGE SORT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
WHAT IS MERGE SORT?
------------------------------------------------
Merge Sort is a divide-and-conquer based sorting algorithm.

The main idea is:
- Divide the array into two halves
- Recursively sort each half
- Merge the two sorted halves into one sorted array

------------------------------------------------
DIVIDE AND CONQUER STRATEGY:
------------------------------------------------
1. Divide:
   - Split the array into two halves until each subarray
     has only one element.

2. Conquer:
   - Sort the smaller subarrays recursively.

3. Combine (Merge):
   - Merge two sorted subarrays into one sorted array.

------------------------------------------------
WHY MERGE SORT WORKS:
------------------------------------------------
- A single element is always sorted.
- By merging sorted subarrays carefully, we get a fully
  sorted array.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Space Complexity:
- O(n) → Requires extra space for merging

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Merge Sort is a stable sorting algorithm.
- Guaranteed O(n log n) time complexity.
- Preferred when consistent performance is required.
- Not an in-place sorting algorithm (needs extra memory).

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


def merge_sort(arr):
    """
    Sorts the given list in ascending order using Merge Sort.

    Parameters:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list
    """

    # Base case:
    # If the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # ------------------------------------------------
    # DIVIDE STEP
    # ------------------------------------------------

    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into left and right halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # ------------------------------------------------
    # CONQUER STEP (RECURSION)
    # ------------------------------------------------

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # ------------------------------------------------
    # COMBINE STEP (MERGE)
    # ------------------------------------------------

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
    left (list): First sorted list
    right (list): Second sorted list

    Returns:
    list: Merged sorted list
    """

    merged = []  # Temporary list to store merged result
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list

    # Compare elements from both lists
    while i < len(left) and j < len(right):

        # Take smaller element and add to merged list
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left list (if any)
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add remaining elements from right list (if any)
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [38, 27, 43, 3, 9, 82, 10]

    # Print original array
    print("Original array:", data)

    # Call merge sort function
    sorted_data = merge_sort(data)

    # Print sorted array
    print("Sorted array:", sorted_data)
