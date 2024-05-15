class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()

        for r, row in enumerate(mat):
            for c, col in enumerate(row):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
                    
        row_len = len(mat)
        col_len = len(mat[0])

        while q:
            r,c = q.popleft()
            for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                n_r = r + dx
                n_c = c + dy

                if n_r < 0 or n_r >= row_len or n_c < 0 or n_c >= col_len or mat[n_r][n_c] != -1:
                    continue
                
                mat[n_r][n_c] = mat[r][c] + 1
                q.append((n_r, n_c))

        return mat

# bfs from all 0s and if a 1 is found update the count
# Time complexety O(n * m)
# space complexity O(n * m)
# mayb use dp for O(1) space complex??
# 