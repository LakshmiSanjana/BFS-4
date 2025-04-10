# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def countMines(board,x,y):
            cnt = 0
            for d in dirs:
                nr = x+d[0]
                nc = y + d[1]
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == 'M':
                    cnt += 1   
            
            return cnt

        def dfs(x,y):
            # base
            if not ( 0<= x < m and 0 <= y < n) or board[x][y] != 'E':
                return

            #logic
            count = countMines(board,x,y)
            if count > 0:
                board[x][y] = str(count)
            
            else:
                board[x][y] = 'B'
                for d in dirs:
                    dfs(x+d[0], y+d[1])


        dirs = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

        x = click[0]
        y = click[1]

        m = len(board)
        n = len(board[0])

        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        dfs(x,y)

        return board


# TC: 0(m * n)
# SC: O(m * n) for the rec stack



#----------------------------------------------------



class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def countMines(board,x,y):
            cnt = 0
            for d in dirs:
                nr = x+d[0]
                nc = y + d[1]
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == 'M':
                    cnt += 1   
            
            return cnt

        dirs = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        q = deque()
        m = len(board)
        n = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        q.append(click)
        board[click[0]][click[1]] = 'B'

        while q:
            curr = q.popleft()
            count = countMines(board, curr[0], curr[1])
            if count == 0:
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == 'E':
                        q.append([nr,nc])
                        board[nr][nc] = 'B'

            else:
                board[curr[0]][curr[1]] = str(count)
        
        return board

# TC: 0(m * n)
# SC: O(m * n) for the queue
        