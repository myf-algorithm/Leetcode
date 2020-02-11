n = input()
vc1, vb1, vj1, e, vc2, vb2, vj2 = 0, 0, 0, 0, 0, 0, 0
for i in range(int(n)):
    a = input().split()
    if a[0] == 'C' and a[1] == 'J':
        vc1 += 1
    elif a[0] == 'B' and a[1] == 'C':
        vb1 += 1
    elif a[0] == 'J' and a[1] == 'B':
        vj1 += 1
    elif a[0] == 'C' and a[1] == 'B':
        vb2 += 1
    elif a[0] == 'B' and a[1] == 'J':
        vj2 += 1
    elif a[0] == 'J' and a[1] == 'C':
        vc2 += 1
    else:
        e += 1
print(vc1 + vb1 + vj1, e, int(n) - e - vc1 - vb1 - vj1)
print(vc2 + vb2 + vj2, e, int(n) - e - vc2 - vb2 - vj2)
if vb1 >= vc1 and vb1 >= vj1:
    s = 'B'
elif vc1 >= vj1 and vc1 > vb1:
    s = 'C'
else:
    s = 'J'
if vb2 >= vc2 and vb2 >= vj2:
    s1 = 'B'
elif vc2 >= vj2 and vc2 > vb2:
    s1 = 'C'
else:
    s1 = 'J'
print(s, s1)

"""
#include <iostream>
 
using namespace std;
 
typedef struct node{
	char a;
	char b;
}Node;
 
typedef struct  _node{
	char a;
	int m;
	int n;
}nn;
 
#define max 100001
int main(int argc,const char *argv[])
{
	int m;
	cin>>m;
	Node a[max];
	for(int i=0;i<m;i++){
		cin>>a[i].a>>a[i].b;
	}
    
	nn b[3];
	b[0].a='B';b[0].m=0;b[0].n=0;
	b[1].a='C';b[1].m=0;b[1].n=0;
	b[2].a='J';b[2].m=0;b[2].n=0;
	
	int p=0;
	for(int j=0;j<m;j++)
	{
		if(a[j].a=='C'){
			if(a[j].b=='J'){
				b[1].m++;
			}else if(a[j].b=='C'){
				p++; 
			}else{
				b[0].n++;
			}
		}else if(a[j].a=='J'){
			if(a[j].b=='B'){
				b[2].m++;
			}else if(a[j].b=='J'){
				p++;
			}else{
				b[1].n++;
			}
		}else{
			if(a[j].b=='C'){
				b[0].m++;
			}else if(a[j].b=='B'){
				p++;
			}else{
				b[2].n++;
			}
		}
	}
	
	cout<<b[0].m+b[1].m+b[2].m<<" ";
	cout<<p<<" "<<b[0].n+b[1].n+b[2].n;
	cout<<endl;
	
	cout<<b[0].n+b[1].n+b[2].n<<" ";
	cout<<p<<" "<<b[0].m+b[1].m+b[2].m;
	cout<<endl;
	
	if(b[0].m>=b[1].m){
		if(b[0].m>=b[2].m){
			cout<<b[0].a;
		}else{
			cout<<b[2].a;
		}
	}else{
		if(b[1].m>=b[2].m){
			cout<<b[1].a;
		}else{
			cout<<b[2].a;
		}
	}
 
	cout<<" ";
	
	if(b[0].n>=b[1].n){
		if(b[0].n>=b[2].n){
			cout<<b[0].a;
		}else{
			cout<<b[2].a;
		}
	}else{
		if(b[1].n>=b[2].n){
			cout<<b[1].a;
		}else{
			cout<<b[2].a;
		}
	}
	
	return 0;
}
"""