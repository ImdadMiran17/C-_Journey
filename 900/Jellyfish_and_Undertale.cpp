#include<bits/stdc++.h>
using namespace std;

int main(void){
    int t;
    cin>>t;
    while(t--){
       int n = 0, a = 0, b = 0;
	   long long ans = 0;
	   scanf("%d %d %d", &a, &b, &n);
		ans = b;
	for(int i = 0, x = 0 ; i < n ; i ++){
		scanf("%d", &x);
		ans += min(a - 1, x);
	}
	printf("%lld\n", ans);
}
return 0;
}
