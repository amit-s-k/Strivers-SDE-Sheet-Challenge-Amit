def missingAndRepeating(arr, n):
    freq = {}
    for i in range(n):
        freq[i+1]=0
    for ele in arr:
        if ele in freq:
            freq[ele]=freq[ele]+1
        else:
            freq[ele]=1
    repeating = -1
    missing = -1
    for key in freq:
        if freq[key]==0:
           missing = key
        elif freq[key]==2:
            repeating = key

    return [missing,repeating]