"""
SORT 0s, 1s AND 2s
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array consisting only of 0s, 1s, and 2s,
sort the array in ascending order.

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:  arr = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

------------------------------------------------
APPROACH 1: BRUTE FORCE (SORTING)
------------------------------------------------
- Simply sort the array using a built-in sorting method.

TIME COMPLEXITY:
- O(n log n)

SPACE COMPLEXITY:
- O(1) or O(n) depending on sorting implementation

WHY IT IS NOT IDEAL:
- Does not use the special property of having only 0s, 1s, and 2s.

------------------------------------------------
APPROACH 2: BETTER (COUNTING)
------------------------------------------------
- Count the number of 0s, 1s, and 2s.
- Overwrite the array with counted values.

TIME COMPLEXITY:
- O(n)

SPACE COMPLEXITY:
- O(1)

------------------------------------------------
APPROACH 3: OPTIMAL (DUTCH NATIONAL FLAG ALGORITHM)
------------------------------------------------
- Use three pointers: low, mid, high.
- Place:
  0s at the beginning,
  1s in the middle,
  2s at the end.
- Perform sorting in a single pass.

TIME COMPLEXITY:
- O(n)

SPACE COMPLEXITY:
- O(1)

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Dutch National Flag algorithm is the expected solution.
- Asked very frequently in interviews.
- Single-pass and in-place solution.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# APPROACH 1: BRUTE FORCE
# ------------------------------------------------
def sort_bruteforce(arr):
    """
    Sorts the array using built-in sort.

    Parameters:
    arr (list): List containing 0s, 1s, and 2s

    Returns:
    None (modifies array in-place)
    """

    arr.sort()


# ------------------------------------------------
# APPROACH 2: BETTER (COUNTING METHOD)
# ------------------------------------------------
def sort_better(arr):
    """
    Sorts the array by counting occurrences of 0s, 1s, and 2s.

    Parameters:
    arr (list): List containing 0s, 1s, and 2s

    Returns:
    None (modifies array in-place)
    """

    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Count occurrences
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    index = 0

    # Place 0s
    for _ in range(count_0):
        arr[index] = 0
        index += 1

    # Place 1s
    for _ in range(count_1):
        arr[index] = 1
        index += 1

    # Place 2s
    for _ in range(count_2):
        arr[index] = 2
        index += 1


# ------------------------------------------------
# APPROACH 3: OPTIMAL (DUTCH NATIONAL FLAG)
# ------------------------------------------------
def sort_optimal(arr):
    """
    Sorts the array using Dutch National Flag algorithm.

    Parameters:
    arr (list): List containing 0s, 1s, and 2s

    Returns:
    None (modifies array in-place)
    """

    low = 0
    mid = 0
    high = len(arr) - 1

    # Traverse the array
    while mid <= high:

        # If element is 0, swap with low
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        # If element is 1, move mid
        elif arr[mid] == 1:
            mid += 1

        # If element is 2, swap with high
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    arr1 = [2, 0, 2, 1, 1, 0]
    arr2 = arr1.copy()
    arr3 = arr1.copy()

    print("Original array:", arr1)

    sort_bruteforce(arr1)
    print("Brute Force Sorted:", arr1)

    sort_better(arr2)
    print("Better Approach Sorted:", arr2)

    sort_optimal(arr3)
    print("Optimal Approach Sorted:", arr3)
