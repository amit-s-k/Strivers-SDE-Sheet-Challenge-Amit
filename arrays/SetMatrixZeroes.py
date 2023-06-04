from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    # Write your code here.
    rows = len(matrix)
    cols = len(matrix[0])
    zeroRows = set()
    zeroCols = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRows.add(i)
                zeroCols.add(j)

    for index in zeroRows:
        matrix[index] = [0] * cols
    for colIndex in zeroCols:
        for r in range(rows):
            matrix[r][colIndex] = 0
if __name__=="__main__":
    matrix=[[7,19,3],[4,21,0]]
    setZeros(matrix)
    print(matrix)