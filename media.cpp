# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
A = ["uvwxyz"]
B = 1
C = 5

A=[list(map(ord,a.lower())) for a in A]

def kmp(a):
    table=[0]
    g=0    
    for i in a[1:]:
        while g and a[g]!=i:
            g=table[g-1]            
        g+=a[g]==i
        table+=[g]
    return table 
tables=[kmp(a) for a in A]



def dp(i,mask):
    
    if sum(j==51 for j in mask)>B:
        return 0
                
    if i==C:
        return sum(j==51 for j in mask)==B
    
    res=0    
    for nxt in range(97,97+26):
        mask1=list(mask)
        for k in range(n):
            l=mask1[k]
            if l!=51:                
                while l and A[k][l]!=nxt:                    
                    l=tables[k][l-1]
                l+=A[k][l]==nxt
                mask1[k]=[l,51][l==len(A[k])]
        res+=dp(i+1,tuple(mask1)) 
    return res
                
n=len(A)

print(dp(0,(0,)*n))
