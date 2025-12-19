def sortedArray(a: [int], b: [int]) -> [int]:
    """
    Returns the UNION of two sorted arrays.
    The result contains all unique elements in sorted order.
    """

    # Pointer for array a
    i = 0

    # Pointer for array b
    j = 0

    # Result list to store union elements
    result = []

    # Traverse both arrays until one is exhausted
    while i < len(a) and j < len(b):

        # If current element of a is smaller or equal
        if a[i] <= b[j]:

            # Add a[i] only if result is empty
            # or last added element is different (avoid duplicates)
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])

            # Move pointer i forward
            i += 1

        # If current element of b is smaller
        else:

            # Add b[j] only if result is empty
            # or last added element is different (avoid duplicates)
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])

            # Move pointer j forward
            j += 1

    # Add remaining elements from array a (if any)
    while i < len(a):

        # Avoid adding duplicates
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])

        i += 1

    # Add remaining elements from array b (if any)
    while j < len(b):

        # Avoid adding duplicates
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])

        j += 1

    # Return the union of both arrays
    return result


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input arrays (sorted)
    a = [1, 2, 2, 3, 5]
    b = [2, 3, 4, 6]

    print("Array A:", a)
    print("Array B:", b)

    # Call the function
    union_result = sortedArray(a, b)

    print("Union of two sorted arrays:", union_result)
