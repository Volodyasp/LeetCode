class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        # P + N = total
        # P - N = target
        # 2P = total + target
        if (total + target) % 2 != 0 or (total + target) < 0:
            return 0

        P = (total + target) // 2
        
        dp = [0] * (P + 1)
        dp[0] = 1

        for num in nums: 
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[P]
