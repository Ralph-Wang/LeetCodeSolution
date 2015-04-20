class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * n

        for j in xrange(n):
            if s[:j+1] in wordDict:
                dp[j] = True
            else:
                for i in xrange(j):
                    if dp[i] and s[i+1:j+1] in wordDict:
                        dp[j] = True
                        break

        return dp[n-1]


cases = [
        ('leetcode', {'leet', 'code'}, True),
        ('aaaaaaa', {'aaaa', 'aaa'}, True),
        ('aaaaaaa', {'aaaa'}, False),
        ]

sl = Solution()
for s, dict , expect in cases:
    assert sl.wordBreak(s, dict) is expect
