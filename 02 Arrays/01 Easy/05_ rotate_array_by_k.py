"""
ROTATE ARRAY BY K POSITIONS (RIGHT ROTATION)
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers and a value K, rotate the
array to the right by K positions.

Right rotation means:
- Each element is shifted to the right by K positions.
- Elements that fall off the end come back at the front.

------------------------------------------------
APPROACH (OPTIMAL - REVERSAL METHOD):
------------------------------------------------
We use the array reversal technique:

1. Reverse the entire array.
2. Reverse the first K elements.
3. Reverse the remaining n-K elements.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Reversing the array rearranges element positions
  correctly without extra space.
- This achieves rotation in O(n) time and O(1) space.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n)

Space Complexity:
- O(1) → in-place rotation

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- Always reduce K using: K = K % n
- This handles cases where K > n
- This is the optimal solution

------------------------------------------------
EDGE CASES:
------------------------------------------------
- K = 0 → no rotation
- K > n → reduce using modulo
- Empty array → no operation

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def rotate_array(arr, k):
    """
    Rotates the array to the right by k positions.

    Parameters:
    arr (list): List of integers
    k (int): Number of positions to rotate

    Returns:
    None (modifies array in-place)
    """

    n = len(arr)

    # Edge case: empty array or no rotation needed
    if n == 0 or k == 0:
        return

    # Reduce k if it is greater than array length
    k = k % n

    # Step 1: Reverse the entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(arr, k, n - 1)


def reverse(arr, start, end):
    """
    Reverses elements in the array from index start to end.

    Parameters:
    arr (list): List of integers
    start (int): Starting index
    end (int): Ending index
    """

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    data = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Original array:", data)
    print("Rotate by:", k)

    # Rotate array
    rotate_array(data, k)

    print("Array after rotation:", data)