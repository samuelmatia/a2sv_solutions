class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        output = []

        if k > len(s): 
            return []

        p_window = [0] * 26
        window = [0] * 26

        for c in p : 
            p_window[ord(c)-ord('a')] +=1

        for i in range(k):
            window[ord(s[i]) - ord('a')] += 1

        if p_window == window : 
            output.append(0)

        left = 1
        for right in range(k, len(s)) : 
            window[ord(s[right])- ord('a')] += 1
            window[ord(s[left-1])- ord('a')] -= 1

            if window == p_window : 
                output.append(left)
            
            left += 1

        return output



       

        