def uniquePaths(m, n):
	if m==1 and n==1:
		return 1
	dp =[]
	for i in range(m):
		temp = []
		for j in range(n):
			temp.append(0)
		dp.append(temp)
	for j in range(n):
		dp[m-1][j]=1
	for i in range(m):
		dp[i][n-1]=1
	dp[m-1][n-1] = 0

	for j in range(n-2,-1,-1):
		for i in range(m-2,-1,-1):
			dp[i][j] = dp[i+1][j] + dp[i][j+1]
	return dp[0][0]