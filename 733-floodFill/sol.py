class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q.append((sr, sc))
        start_colour = image[sr][sc]
        if start_colour == color:
            return image

        image[sr][sc] = color

        while q:
            r, c = q.popleft()
            for x, y in dirs:
                nr = r + x
                nc = c + y
                if nr < 0 or nr >= len(image) or nc < 0 or nc >= len(image[0]):
                    continue
                if image[nr][nc] == start_colour:
                    q.append((nr, nc))
                    image[nr][nc] = color

        return image
    
    
# 
# Time Complexity: O(mn) -> vist every element once when performing bfs