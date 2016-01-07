class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = list(pattern)
        s = str.split(" ")

        if len(p) != len(s):
            return False

        table_p = {}
        table_s = {}
        while p and s:
            cur_p = p.pop()
            cur_s = s.pop()
            if cur_p not in table_p:
                table_p[cur_p] = cur_s
            elif cur_s != table_p[cur_p]:
                return False
            if cur_s not in table_s:
                table_s[cur_s] = cur_p
            elif cur_p != table_s[cur_s]:
                return False
        return True

