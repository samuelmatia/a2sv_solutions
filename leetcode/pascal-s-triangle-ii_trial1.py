class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]

        for i in range(rowIndex) : 
            row = [0] + output[-1] + [0]
            result = []
            for j in range(len(output[-1])+1) : 
                add = row[j] + row[j+1]
                result.append(add)

            output.append(result)

        return output[rowIndex]
        