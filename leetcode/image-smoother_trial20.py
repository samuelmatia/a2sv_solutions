class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        directions = [(-1,0),(0,-1),(1,0),(0,1),
                      (-1,-1),(1,1),(1,-1),(-1,1)]
        
        n = len(img)
        m = len(img[0])
        
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                
                total = img[i][j]
                count = 1
                
                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy
                    
                    if 0 <= nx < n and 0 <= ny < m:
                        total += img[nx][ny]
                        count += 1
                
                ans[i][j] = total // count 
        
        return ans