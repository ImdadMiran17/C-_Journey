#include<bits/stdc++.h>
using namespace std;

int main(void){
    int t;
    cin>>t;
    while(t--){
     long long n,k,x;
	   cin>>n>>k>>x;
	   if(2*x>= k*(k+1) && 2*x<=n*(n+1)-(n-k)*(n-k+1)){
	   	cout<<"YES\n";
	   }
	   else{
	   	cout<<"NO\n";
	   }
}
return 0;
}
