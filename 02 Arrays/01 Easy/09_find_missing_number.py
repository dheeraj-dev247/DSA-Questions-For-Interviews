"""
FIND THE MISSING NUMBER IN AN ARRAY
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an array containing n distinct numbers
taken from the range 0 to n.

Exactly one number is missing from the array.
Find and return the missing number.

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:  arr = [3, 0, 1]
Output: 2

Explanation:
Numbers should be from 0 to 3 → {0,1,2,3}
But 2 is missing.

------------------------------------------------
APPROACH (OPTIMAL - SUM FORMULA):
------------------------------------------------
1. If numbers are from 0 to n, the expected sum is:
   n * (n + 1) // 2

2. Compute the actual sum of elements in the array.

3. The missing number is:
   expected_sum - actual_sum

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Only one number is missing.
- All other numbers are distinct.
- Difference between expected and actual sum
  directly gives the missing number.

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
- This is the most common solution.
- Works only when numbers are in range 0 to n.
- No extra space required.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Missing number is 0
- Missing number is n
- Array of size 1

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def find_missing_number(arr):
    """
    Finds the missing number in the array.

    Parameters:
    arr (list): List of integers from range 0 to n with one missing

    Returns:
    int: Missing number
    """

    n = len(arr)

    # Expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2

    # Actual sum of array elements
    actual_sum = sum(arr)

    # Missing number is the difference
    missing_number = expected_sum - actual_sum

    return missing_number


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input array
    arr = [3, 0, 1]

    print("Array:", arr)

    # Find missing number
    result = find_missing_number(arr)

    print("Missing number:", result)
