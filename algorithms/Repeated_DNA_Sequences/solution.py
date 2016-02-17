class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        once = set()
        res = set()
        for i in xrange(n - 9):
            subs = s[i:i + 10]
            [once, res][subs in once].add(subs)
        return list(res)
