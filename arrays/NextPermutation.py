def nextPermutation(permutation, n):
    ans = []
    firstDecreasingElementIndex = -1
    for i in range(n-2,-1,-1):
        if permutation[i]<permutation[i+1]:
            firstDecreasingElementIndex=i
            break
    largerEleIndex =-1
    for i in range(firstDecreasingElementIndex+1,n):
        if permutation[i]<=permutation[firstDecreasingElementIndex]:
            largerEleIndex=i-1
            break
    if firstDecreasingElementIndex != -1:
        temp = permutation[firstDecreasingElementIndex]
        permutation[firstDecreasingElementIndex]=permutation[largerEleIndex]
        permutation[largerEleIndex]=temp
    k=firstDecreasingElementIndex+1
    j=n-1
    while k<j:
        temp = permutation[k]
        permutation[k]=permutation[j]
        permutation[j]=temp
        k+=1
        j-=1
    ans.extend(permutation)
    return ans
if __name__=="__main__":
    permutation = [3,2,1]
    print(nextPermutation(permutation,len(permutation)))