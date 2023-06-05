def rotateMatrix(mat, n, m):
    top =0
    bottom = n-1
    left = 0
    right = m-1
    while top < bottom and left < right:
        for i in range(top,bottom):
            swap(mat,i,left,i+1,left)
        for i in range(left,right):
            swap(mat,bottom,i,bottom,i+1)
        for i in range(bottom,top,-1):
            swap(mat,i,right,i-1,right)
        for i in range(right,left+1,-1):
            swap(mat,top,i,top,i-1)
        top+=1
        bottom-=1
        left+=1
        right-=1
def swap (mat,row1,col1,row2,col2):
    temp = mat[row1][col1]
    mat[row1][col1]=mat[row2][col2]
    mat[row2][col2]=temp
if __name__=="__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    n=len(mat)
    m=len(mat[0])
    rotateMatrix(mat,n,m)
    print(mat)