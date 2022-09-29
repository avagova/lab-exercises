def solution(arr):
    ind = []
    res = ""
    for j in range(len(arr)):
        if arr[j] == '(':
            ind.insert(0,j)
        elif arr[j] == ')':
            arr = arr[:ind[0]+1] + arr[ind[0]+1:j][::-1] + arr[j:]
            del ind[0]
    return arr.replace('(','').replace(')','')
