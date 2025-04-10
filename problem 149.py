# https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        if board == None or len(board) == 0:
            return 0
        
        n = len(board)

        r = n-1
        c = 0
        arr = [0] * ( n*n)
        dirs = True
        idx = 0
        
        while idx < n*n:
            if board[r][c] == -1:
                arr[idx] = board[r][c]
            else:
                arr[idx] = board[r][c] - 1
            
            idx +=1

            if dirs:
                c+=1
                if c == n:
                    dirs = False
                    r-=1
                    c-=1
            else:
                c-=1
                if c == -1:
                    dirs = True
                    r-=1
                    c+=1

        q = deque()
        q.append(0)
        arr[0] = -2
        moves = 0

        while q:
            len_q = len(q)
            
            for i in range(len_q):
                curr = q.popleft()
                if curr == n*n - 1:
                    return moves
                
                for i in range(1,7):
                    newIdx = curr + i
                    if newIdx < n*n and arr[newIdx] != -2:
                        if arr[newIdx] == -1:
                            q.append(newIdx)
                        else:
                            q.append(arr[newIdx])
                        
                        arr[newIdx] = -2
            
            moves+=1
        
        return -1

# TC: O(n*2)
# SC: O(n*2)