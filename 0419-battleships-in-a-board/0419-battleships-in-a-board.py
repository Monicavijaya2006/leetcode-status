class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def bfs(row,col):
            vis[row][col]=True
            queue=[(row,col)]
            area=1
            while queue:
                row,col=queue.pop(0)
                drs=[(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dy in drs:
                    nrow=row+dr
                    ncol=col+dy
                    if 0<=nrow<len(board) and 0<=ncol<len(board[0]) and not vis[nrow][ncol] and board[nrow][ncol]=='X':
                        vis[nrow][ncol]=True
                        area+=1
                        queue.append((nrow,ncol))
        vis=[[False]*len(board[0]) for _ in range(len(board))]
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X' and not vis[i][j]:
                    count+=1
                    bfs(i,j)
        return count
                    