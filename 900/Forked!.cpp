#include<bits/stdc++.h>
using namespace std;

int dx[4] = {-1, 1, -1, 1};
int dy[4] = {-1, -1, 1, 1};

int main(void){
    int t;
    cin>>t;
    while(t--){
        int a,b;
		cin>>a>>b;
		int x1,y1,x2,y2;
		cin>>x1>>y1>>x2>>y2;
		set<pair<int, int>> str1, str2;
		for(int i = 0; i < 4; i++){
			str1.insert({x1+dx[i]*a, y1+dy[i]*b});
			str2.insert({x2+dx[i]*a, y2+dy[i]*b});
			str1.insert({x1+dx[i]*b, y1+dy[i]*a});
			str2.insert({x2+dx[i]*b, y2+dy[i]*a});
		}

		int ans = 0;
		for (auto x: str1){
			if (str2.find(x) != str2.end()){
				ans++;
			}
		}

		cout<<ans<<'\n';

}
return 0;
}
