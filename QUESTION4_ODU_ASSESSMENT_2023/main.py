def findLongestRepeatingSubSeq(X):
    m = len(X)
    # Create and initialize DP table
    dp = [[0 for j in range(m+1)] for i in range(m+1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1, m+1):
        for j in range(1, m+1):
            # If characters match and indexes are not same
            if X[i-1]== X[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            # If characters do not match
            else:
                dp[i][j] =max(dp[i][j-1], dp[i-1][j])

    return dp[m][m]

# Driver program to check above function
X=input("Enter a string:\n")
print("The length of the largest subsequence that repeats itself is: ", findLongestRepeatingSubSeq(X))
