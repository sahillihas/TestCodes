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

//----
Questions:
Fractional knapsack
Scrambled string
Water level



scramble string :- 
int dp[55][55][55][55];
int solve(int i1,int j1,int i2,int j2,const string A, const string B)
{
    if(i1 == j1)
    {
        return i2==j2 && A[i1]==B[i2];
    }

    if(dp[i1][j1][i2][j2]!=-1)
    return dp[i1][j1][i2][j2];

    int ans=0;

    for(int k=i1;k<j1;k++)
    {
        ans|=solve(i1,k,i2,i2+(k-i1),A,B)&solve(k+1,j1,i2+(k-i1)+1,j2,A,B);//No swap;
        ans|=solve(i1,k,j2-(k-i1),j2,A,B)&solve(k+1,j1,i2,j2-(k-i1)-1,A,B);//Swap;

    }

    return dp[i1][j1][i2][j2]=ans;
}
int Solution::isScramble(const string A, const string B) {
    memset(dp,-1,sizeof(dp));

    int n=A.size();

    return solve(0,n-1,0,n-1,A,B);
}


Solution 2 (question konsa he vo dekh lena idk)
#include <bits/stdc++.h>
using namespace std;
int minimumDivisions(vector<int>& A, int B) {
    int n = A.size();
    priority_queue<int>pq;
    for(auto it:A){
        pq.push(it);
    }
    int count = 0;
    int i = 0;
    while(B>0 && !pq.empty()){
        if(pq.top()<=B){
            B-=pq.top();
            pq.pop();
        }
        else {
            count++;
            int val = pq.top()/2;
            pq.pop();
            pq.push(val);
        }
    }
    return B==0 ? count:-1;
}

int main() {
    int n, B;
    B = 10;
    vector<int>A =  {1,32,1};
    int minDivisions = minimumDivisions(A, B);
    if (minDivisions == INT_MAX) {
        cout<<"-1";
    } else {
        std::cout << "Minimum number of divisions needed: " << minDivisions << std::endl;
    }

    return 0;
}

    
