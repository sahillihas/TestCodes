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

# Mask Updates
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

bool helper(ll P, vector<vector<ll>> &A, ll S)
{
	ll k = A[0].size();
	vector<ll> minMaskCost((1 << k), 1e18);
	ll n = A.size();

	for (ll i = 0; i < n; i++)
	{
		for (ll mask = 0; mask < (1 << k); mask++)
		{
			ll cost = 0;
			for (ll j = 0; j < k; j++)
			{
				if ((mask >> j) & 1)
				{
					cost += (P + A[i][j] - 1) / (A[i][j]);
				}
			}
			minMaskCost[mask] = min(minMaskCost[mask], cost);
		}
	}
	ll minCost = INT64_MAX;
	for (ll mask = 0; mask < (1 << k); mask++)
	{
		ll invertmask = 0;
		for (ll j = 0; j < k; j++)
		{
			if (!((mask >> j) & 1))
			{
				invertmask += (1 << j);
			}
		}
		minCost = min(minCost, minMaskCost[mask] + minMaskCost[invertmask]);
	}

	if (minCost <= S)return 1;
	else return 0;
}
int Solution(vector<vector<ll>> A, ll S)
{
	ll l = 0;
	ll r = 1e18;
	ll maxSize = -1;
	while (r - l >= 0)
	{
		ll mid = (l + r) / 2;
		if (helper(mid, A, S))
		{
			l = mid + 1;
			maxSize = mid;
		}
		else {
			r = mid - 1;
		}
	}

	return maxSize;
}
void solve()
{
	vector<vector<ll>> A = {{9, 4, 1}, {2, 5, 10}, {6, 8, 3}};
	ll S = 10;
	// vector<vector<ll>> A = {{1, 4}, {4, 1}};
	// ll S = 10;
	cout << Solution(A, S) << endl;
}
int main()
{
	solve();
}
    
