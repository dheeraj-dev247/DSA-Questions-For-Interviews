"""
BEST TIME TO BUY AND SELL STOCK (LEETCODE 121)
DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an array prices where prices[i]
represents the price of a stock on the ith day.

You want to maximize your profit by choosing:
- One day to buy the stock
- A later day to sell the stock

Return the maximum profit.
If no profit is possible, return 0.

------------------------------------------------
EXAMPLES:
------------------------------------------------
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation:
Buy at price 1 and sell at price 6 → profit = 5

Input:  prices = [7,6,4,3,1]
Output: 0
Explanation:
Prices only decrease → no profit possible

------------------------------------------------
CONSTRAINTS:
------------------------------------------------
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

------------------------------------------------
APPROACH 1: BRUTE FORCE (DOUBLE LOOP)
------------------------------------------------
INTUITION:
------------------------------------------------
- Try every possible pair of days.
- For each day i, consider selling on every
  future day j > i.
- Compute profit = prices[j] - prices[i].
- Track the maximum profit.

------------------------------------------------
WHY IT WORKS:
------------------------------------------------
- Ensures buy happens before sell.
- Examines all valid possibilities.

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n²)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def max_profit_bruteforce(prices):
    """
    Brute force solution using two loops.
    """

    max_profit = 0
    n = len(prices)

    # Choose buying day
    for i in range(n):

        # Choose selling day after buying day
        for j in range(i + 1, n):

            # If profitable transaction
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

    return max_profit


"""
------------------------------------------------
APPROACH 2: OPTIMAL (ONE PASS / GREEDY)
------------------------------------------------
INTUITION:
------------------------------------------------
- Track the minimum price seen so far.
- At each day, calculate profit if sold today.
- Update the maximum profit.
- Always buy at the lowest price before selling.

------------------------------------------------
CORE IDEA:
------------------------------------------------
Buy low → sell high (in the future).

------------------------------------------------
ALGORITHM STEPS:
------------------------------------------------
1. Initialize min_price = infinity
2. Initialize max_profit = 0
3. Traverse prices:
   - Update min_price
   - Compute profit = current_price - min_price
   - Update max_profit

------------------------------------------------
TIME & SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

------------------------------------------------
CODE:
------------------------------------------------
"""


def max_profit_optimal(prices):
    """
    Optimal solution using a single pass.
    """

    min_price = float("inf")  # Lowest price so far
    max_profit = 0  # Maximum profit so far

    # Traverse price list
    for price in prices:

        # Update minimum price
        min_price = min(min_price, price)

        # Calculate profit if sold today
        profit = price - min_price

        # Update maximum profit
        max_profit = max(max_profit, profit)

    return max_profit


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    print("Prices:", prices1)
    print("Brute Force Profit:", max_profit_bruteforce(prices1))
    print("Optimal Profit:", max_profit_optimal(prices1))

    print()

    print("Prices:", prices2)
    print("Brute Force Profit:", max_profit_bruteforce(prices2))
    print("Optimal Profit:", max_profit_optimal(prices2))
