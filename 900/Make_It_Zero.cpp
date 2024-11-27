#include<bits/stdc++.h>
using namespace std;

int main(void){
    int t;
    cin>>t;
    while(t--){
       int n;
	   cin >> n;
	   vector<int> arr(n);
	   for(int i = 0; i < n; i++){
	       cin >> arr[i];
	   }
	   if(n & 1){
		cout << "4" << "\n";
		cout << 1 << " " << n-1 << "\n";
		cout << 1 << " " << n-1 << "\n";
		cout << n-1 << " " << n << "\n";
		cout << n-1 << " " << n << "\n";
	   }else{
		cout << "2" << "\n";
		cout << 1 << " " << n << "\n";
		cout << 1 << " " << n << "\n";
	   }
}
return 0;
}
