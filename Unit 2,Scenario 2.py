# Number of Ways to Make Change using Dynamic Programming

class CoinChange:

    def count_ways(self, coins, amount):

        # Create DP array
        dp = [0] * (amount + 1)

        # One way to make amount 0
        dp[0] = 1

        # Calculate number of ways
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]

        return dp[amount]


# Main Program

coins = list(map(int, input("Enter coin values (space separated): ").split()))
amount = int(input("Enter target amount: "))

obj = CoinChange()

ways = obj.count_ways(coins, amount)

print("\nTotal Ways =", ways)
Comment:-
Enter coin values (space separated): 1 2 5
Enter target amount: 5

Total Ways = 4
