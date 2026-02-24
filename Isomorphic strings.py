class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for i, j in zip(s,t): #iterate over the s and t simultaneously
            if i in st: #for i in st
                if st[i]!=j: #if previous map of i != current mapping
                    return False
            else:
                st[i]=j #map the j to i
            if j in ts:
                if ts[j]!=i:
                    return False
            else:
                ts[j]=i
        return True

        
