# right
def maxProfit2(prices):
    # Get the number of days (length of the prices list)
    n = len(prices)

    # Initialize the minimum price to the first day's price
    mini = prices[0]

    # Initialize the maximum profit to 0
    profit = 0

    # Iterate over each day's price
    for i in range(1, n):
        # Calculate the potential profit if we sell on day i
        cost = prices[i] - mini

        # Update the maximum profit if the current potential profit is higher
        profit = max(profit, cost)

        # Update the minimum price encountered so far
        mini = min(mini, prices[i])

    # Return the maximum profit found
    return profit


# wrong
def maxProfit(prices):
    # Step 1: Get the total number of days (prices).
    n = len(prices)

    # Step 2: Assume you buy on the first day (initially the cheapest).
    buy = prices[0]

    # Step 3: Start with zero profit because no candy is sold yet.
    profit = 0

    # Step 4: Go through each day starting from the second day.
    for i in range(1, n):
        # Step 5: If today's price is cheaper than what you bought it for, "pretend" to buy today.
        if prices[i] < buy:
            buy = prices[i]  # Update the "buy" price to today's lower price.

        # Step 6: If selling today gives more profit than before, update the profit.
        elif prices[i] - buy > profit:
            profit = prices[i] - buy  # Calculate new profit and update.

    # Step 7: Return the maximum profit you could have made.
    return profit


def main():
    n = int(input())
    arr = [int(x) for x in input().split(",")]
    print(maxProfit(arr))


main()
