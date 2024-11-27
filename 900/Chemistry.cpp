#include<bits/stdc++.h>
using namespace std;

int main(void){
	const int L=26;
    int t;
    cin>>t;
    while(t--){
       int n,k;
	   cin>>n>>k;
	   string s;
	   cin>>s;
	   int V[L]={0}; 
	   for(int i=0; i< s.size(); i++){
		   V[s[i]-'a']++;
	   }
	   int cnt = 0;
	   for(int i=0; i<L; i++){
		cnt += V[i]%2;
	   }

	   puts(cnt<=k+1?"YES":"NO");


}
return 0;
}
