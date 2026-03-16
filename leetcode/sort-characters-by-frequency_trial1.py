class Solution:
    def frequencySort(self, s: str) -> str:
        dico = {}
        for char in s : 
            dico[char] = dico.get(char, 0) + 1

        dico = dict(sorted(dico.items(), key=lambda item : item[1], reverse=True ))
        print(dico)
        output = [""]*len(s)

        idx = 0

        for y, x in enumerate(list(dico.keys())) : 
            for _ in range(list(dico.values())[y]) : 
                output[idx] = x 
            
                idx += 1

        return "".join(output)