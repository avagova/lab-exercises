class Solution:
    def merge(self, l1: List[int], m: int, l2: List[int], n: int) -> None:
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j])
                j+=1
        while i < m:
            res.append(l1[i])
            i+=1
        while j < n:
            res.append(l2[j])
            j+=1
        l1 = res # res-@ chisht zangvaca bayc chgitem xi l1-in chi linum vernagrel
                
          
     
