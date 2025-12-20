"""
TWO SUM PROBLEM
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they
add up to the target.

You may assume that:
- Exactly one solution exists
- You may not use the same element twice

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

------------------------------------------------
APPROACH (OPTIMAL - HASH MAP):
------------------------------------------------
- Use a hash map (dictionary) to store elements
  we have already seen along with their indices.
- For each element:
  1. Calculate the required value:
     required = target - current_element
  2. Check if required exists in the hash map.
     - If yes → solution found
     - If no → store current element in the map

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Hash map allows O(1) average-time lookup.
- We check each element only once.
- Ensures we do not reuse the same element.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n)

Space Complexity:
- O(n)

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- This is the most expected solution in interviews.
- Brute force O(n^2) solution is NOT preferred.
- Order of checking matters (check before insert).

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Negative numbers
- Zero values
- Target formed by first two elements

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def two_sum(nums, target):
    """
    Finds indices of the two numbers that add up to target.

    Parameters:
    nums (list): List of integers
    target (int): Target sum

    Returns:
    list: Indices of the two numbers
    """

    # Dictionary to store number -> index
    seen = {}

    # Traverse the array
    for i in range(len(nums)):

        # Calculate the required value
        required = target - nums[i]

        # Check if required value is already seen
        if required in seen:
            return [seen[required], i]

        # Store current value with its index
        seen[nums[i]] = i

    # As per problem statement, this line will never be reached
    return []


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    print("Array:", nums)
    print("Target:", target)

    result = two_sum(nums, target)

    print("Indices of elements:", result)
