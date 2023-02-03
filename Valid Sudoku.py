class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = set()
        for i in range(9):   
            for j in range(9):
                if board[i][j]=='.':
                    pass
                elif ((str(board[i][j]) + ' r ' + str(i)) not in d) and ((str(board[i][j]) + ' c ' + str(j)) not in d) and ((str(board[i][j]) + ' b ' + str(i//3)+str(j//3)) not in d):
                    d.add(str(board[i][j]) + ' r ' + str(i))
                    d.add(str(board[i][j]) + ' c ' + str(j))
                    d.add(str(board[i][j]) + ' b ' + str(i//3)+str(j//3))
                else:
                    return (False)
                    
                    
        return True
        
