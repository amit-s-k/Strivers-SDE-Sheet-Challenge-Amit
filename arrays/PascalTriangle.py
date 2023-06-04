def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)
                continue
            num = (row[j-1] *(i-(j-1)))//(j)
            if num!=0:
                row.append(num)
            else:
                break
        ans.append(row)
    return ans
if __name__=="__main__":
    n=50
    pascalTriangle = printPascal(n)
    for row in pascalTriangle:
        print(row)
        print("\n")