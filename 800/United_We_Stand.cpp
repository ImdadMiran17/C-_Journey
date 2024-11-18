#include<bits/stdc++.h>
using namespace std;

int main(void){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin >> n;
        vector<int> arr;
        arr.assign(n, 0);
        for(auto& x: arr) cin >> x;
        sort(arr.begin(), arr.end());
        if(arr.back() == arr[0]){
            cout << "-1\n";
        }else {
            int it = 0;
            while(arr[it] == arr[0]) it++;
            cout << it << " " << n - it << "\n";
            for(int j=0; j<it; j++) cout << arr[j] << " ";
            cout << "\n";
            for(int j=it; j<n; j++) cout << arr[j] << " ";
        }
    }
return 0;
}
