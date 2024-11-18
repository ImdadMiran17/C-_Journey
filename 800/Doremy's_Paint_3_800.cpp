#include<bits/stdc++.h>
using namespace std;

int main(void){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin >> n;
        map<int,int> arr;
        for(int i = 1; i <= n; i++){
            int x;
            cin >> x;
            arr[x]++;
        }
        if(arr.size() >= 3){
            puts("NO");
        }else{
            if(abs(arr.begin()->second - arr.rbegin()->second) <= 1){
                puts("YES");
        }else{
            puts("NO");
        }
    }
    }
return 0;
}
