"""
MOVE ALL ZEROS TO THE END OF THE ARRAY
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers, move all the zeros
to the end of the array while maintaining the
relative order of the non-zero elements.

------------------------------------------------
APPROACH (OPTIMAL - TWO POINTER METHOD):
------------------------------------------------
- Use one pointer to track the position where
  the next non-zero element should be placed.
- Traverse the array:
  - If a non-zero element is found, place it
    at the current position and move the pointer.
- After traversal, fill the remaining positions
  with zeros.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Maintains the order of non-zero elements.
- Performs the operation in O(n) time.
- Uses O(1) extra space.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n)

Space Complexity:
- O(1)

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Do NOT use extra arrays.
- Order of non-zero elements must remain same.
- Very common array interview question.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Array with no zeros → unchanged
- Array with all zeros → unchanged
- Empty array → no operation

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def move_zeros_to_end(arr):
    """
    Moves all zeros to the end of the array in-place.

    Parameters:
    arr (list): List of integers

    Returns:
    None (modifies array in-place)
    """

    # Pointer for the position of next non-zero element
    index = 0

    # First pass: move all non-zero elements to the front
    for num in arr:

        # If current element is non-zero
        if num != 0:
            arr[index] = num
            index += 1

    # Second pass: fill remaining positions with zeros
    while index < len(arr):
        arr[index] = 0
        index += 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [0, 1, 0, 3, 12]

    print("Original array:", data)

    # Move zeros to end
    move_zeros_to_end(data)

    print("Array after moving zeros to end:", data)