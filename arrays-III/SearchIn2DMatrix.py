def searchMatrix(matrix: [[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    if rows == 0:
        return False
    low = 0
    high = rows * cols -1
    while low <=high:
        mid = (low + high)//2
        midEle = matrix[mid//cols][mid%cols]
        if target == midEle:
            return True
        else:
            if target < midEle:
                high=mid-1
            else:
                low=mid+1
    return False