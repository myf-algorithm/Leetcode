def read(a):
    res = []
    flag = 0
    tmp = ''
    for i in a:
        if flag == 0 and i == '[':
            flag = 1
            continue
        if flag == 1 and i == ']':
            flag = 0
            res.append(tmp)
            tmp = ''
            continue
        if flag == 1:
            tmp += i
    return res


hands = read(input().strip())
eyes = read(input().strip())
mouse = read(input().strip())

K = int(input())
res = []
for i in range(K):
    output = ""
    a = list(map(int, input().strip().split()))
    if 1 <= a[0] <= len(hands):
        output += hands[a[0] - 1]
    else:
        output = "Are you kidding me? @\/@"
        res.append(output)
        continue
    output += '('
    if 1 <= a[1] <= len(eyes):
        output += eyes[a[1] - 1]
    else:
        output = "Are you kidding me? @\/@"
        res.append(output)
        continue
    if 1 <= a[2] <= len(mouse):
        output += mouse[a[2] - 1]
    else:
        output = "Are you kidding me? @\/@"
        res.append(output)
        continue
    if 1 <= a[3] <= len(eyes):
        output += eyes[a[3] - 1]
    else:
        output = "Are you kidding me? @\/@"
        res.append(output)
        continue
    output += ')'
    if 1 <= a[4] <= len(hands):
        output += hands[a[4] - 1]
    else:
        output = "Are you kidding me? @\/@"
        res.append(output)
        continue
    res.append(output)
print('\n'.join(res))


# OJ上非零返回
"""
#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
 
using namespace std;
 
int main(){
	vector<vector<string> >ans;
	for(int i=0 ;i<3 ;i++){
		vector<string>temp;	 
		string s;
		getline(cin,s);
		for(int j=0 ;j<s.length() ;j++){
			if(s[j]=='['){
				for(int k=j+1 ;k<s.length() ;k++){
					if(s[k]==']'){
						temp.push_back(s.substr(j+1,k-j-1));
						break;
					}
				}
			}
		}
		ans.push_back(temp);
	}

	int n;
	int a,b,c,d,e;
	scanf("%d",&n);
 
	for(int i=0 ;i<n ;i++){
		scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
		if(a<1||b<1||c<1||d<1||e<1||a>ans[0].size()||b>ans[1].size()||c>ans[2].size()||d>ans[1].size()||e>ans[0].size()){
			printf("Are you kidding me? @\\/@\n");
		}else{
			cout<<ans[0][a-1]<<"("<<ans[1][b-1]<<ans[2][c-1]<<ans[1][d-1]<<")"<<ans[0][e-1]<<endl;			
		}
	}
	return 0;
}
"""