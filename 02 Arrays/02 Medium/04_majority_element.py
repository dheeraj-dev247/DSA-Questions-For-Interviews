"""
MAJORITY ELEMENT
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array nums of size n, return the majority
element.

The majority element is the element that appears
more than ⌊n / 2⌋ times.

You may assume that the majority element always
exists in the array.

------------------------------------------------
EXAMPLE:
------------------------------------------------
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2

------------------------------------------------
APPROACH 1: BRUTE FORCE (DOUBLE LOOP)
------------------------------------------------
INTUITION:
------------------------------------------------
- For every element, count how many times it appears.
- If its count exceeds n // 2, it is the majority.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n²)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def majority_element_bruteforce(nums):
    """
    Finds the majority element using brute force.
    """

    n = len(nums)

    # Pick each element as a candidate
    for i in range(n):

        count = 0

        # Count its occurrences
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1

        # Check if it is majority
        if count > n // 2:
            return nums[i]

    return -1  # Will never be reached as majority exists


"""
------------------------------------------------
APPROACH 2: BETTER (HASH MAP / FREQUENCY COUNT)
------------------------------------------------
INTUITION:
------------------------------------------------
- Store frequency of each element in a hash map.
- The element whose frequency exceeds n // 2
  is the majority element.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(k), where k is number of distinct elements

------------------------------------------------
CODE:
------------------------------------------------
"""


def majority_element_hashmap(nums):
    """
    Finds the majority element using a hash map.
    """

    freq = {}
    n = len(nums)

    # Count frequency of each element
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Find the element with frequency > n // 2
    for key, value in freq.items():
        if value > n // 2:
            return key

    return -1


"""
------------------------------------------------
APPROACH 3: OPTIMAL (BOYER-MOORE VOTING ALGORITHM)
------------------------------------------------
CORE INSIGHT:
------------------------------------------------
- Pair different elements and cancel them out.
- The true majority element cannot be fully canceled
  because it appears more than all others combined.

------------------------------------------------
ALGORITHM STEPS:
------------------------------------------------
1. Maintain a candidate and a count.
2. If count becomes 0, pick the current element
   as the new candidate.
3. Increase count if current element equals candidate.
4. Decrease count otherwise.
5. Final candidate is the majority element.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def majority_element_boyer_moore(nums):
    """
    Finds the majority element using Boyer-Moore Voting Algorithm.
    """

    candidate = None
    count = 0

    # Traverse the array
    for num in nums:

        # If no current candidate, pick new one
        if count == 0:
            candidate = num
            count = 1

        # If same as candidate, increase count
        elif num == candidate:
            count += 1

        # If different, decrease count
        else:
            count -= 1

    # Candidate is guaranteed to be majority
    return candidate


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [2, 2, 1, 1, 1, 2, 2]

    print("Array:", nums)

    print("Brute Force Result:", majority_element_bruteforce(nums))

    print("Hash Map Result:", majority_element_hashmap(nums))

    print("Boyer-Moore Result:", majority_element_boyer_moore(nums))
