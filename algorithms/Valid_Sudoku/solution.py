class Solution(object):
    def is_valid(self, board, start, end):
        existed = set()
        x1, y1 = start
        x2, y2 = end
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                if board[i][j] == '.':
                    continue
                if board[i][j] in existed:
                    return False
                else:
                    existed.add(board[i][j])
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid = True
        # line
        for i in xrange(9):
            valid = self.is_valid(board, (i, 0), (i, 8))
            if not valid:
                return valid

        # vertical
        for i in xrange(9):
            valid = self.is_valid(board, (0, i), (8, i))
            if not valid:
                return valid
        # piece
        for i in xrange(0, 7, 3):
            for j in xrange(0, 7, 3):
                valid = self.is_valid(board, (i, j), (i+2, j+2))
                if not valid:
                    return valid

        return valid
