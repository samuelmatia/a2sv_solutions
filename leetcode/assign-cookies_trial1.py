class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        idx_children = 0  
        idx_cookie = 0  
        
        while idx_children < len(g) and idx_cookie < len(s):
            if s[idx_cookie] >= g[idx_children]:
                idx_children += 1  
            idx_cookie += 1  
        
        return idx_children
        