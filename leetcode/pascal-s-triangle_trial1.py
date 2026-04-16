class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(numRows -1) : 
            row = [0] + output[-1] + [0]
            result = []

            for j in range(len(output[-1])+1) :
                add = row[j] + row[j+1]
                result.append(add)

            output.append(result)
        
        return output

        