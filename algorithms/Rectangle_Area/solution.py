class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E > C or F > D or G < A or H < B: # 没有重叠部分
            return abs(A-C) * abs(B-D) + abs(E-G) * abs(F-H)
        X1, Y1 = (min(C, G), min(D, H))
        X2, Y2 = (max(A, E), max(B, F))
        return abs(A-C) * abs(B-D) + abs(E-G) * abs(F-H) - abs(X1-X2) * abs(Y1-Y2)
