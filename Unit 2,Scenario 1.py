# Unique Paths Problem using Dynamic Programming

class UniquePath:

    def find_paths(self, rows, cols):

        # Create DP table
        dp = [[0 for j in range(cols)] for i in range(rows)]

        # First row and first column always have 1 path
        for i in range(rows):
            dp[i][0] = 1

        for j in range(cols):
            dp[0][j] = 1

        # Calculate remaining paths
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows - 1][cols - 1]


# Main Program

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

obj = UniquePath()

result = obj.find_paths(rows, cols)
Comment:-
Enter number of rows: 3
Enter number of columns: 3

Total Unique Paths = 6


