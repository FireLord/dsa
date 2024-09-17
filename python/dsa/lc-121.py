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
    arr = [int(x) for x in input().split(" ")]
    print(maxProfit(arr))

main()