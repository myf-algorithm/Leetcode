a = [int(i) for i in input().strip().split()]
N, L, H = a[0], a[1], a[2]
stu = []
for _ in range(int(N)):
    b = [int(i) for i in input().strip().split()]
    stu.append(b)
type1 = []
type2 = []
type3 = []
type4 = []


def sum(a):
    return -(int(a[1]) + int(a[2])), -int(a[1]), int(a[0])


for i in range(len(stu)):
    if stu[i][1] >= L and stu[i][2] >= L:
        if stu[i][1] >= H and stu[i][2] >= H:
            type1.append(stu[i])
        elif stu[i][1] >= H and stu[i][2] < H:
            type2.append(stu[i])
        elif stu[i][1] < H and stu[i][2] < H and stu[i][1] >= stu[i][2]:
            type3.append(stu[i])
        else:
            type4.append(stu[i])
print(len(type1) + len(type2) + len(type3) + len(type4))
for i in (type1, type2, type3, type4):
    i.sort(key=sum)
    for j in i:
        print(' '.join([str(k) for k in j]))

"""
#define _CRT_SECURE_NO_WARNINGS
 
#include<iostream>
#include <algorithm>
#include <vector>
using namespace std;
class student {
public:
	int level, id, de, cai, total;
};
bool cmp(student& a, student& b) {
	if (a.level != b.level)
		return a.level < b.level;
	else if (a.total != b.total)
		return a.total > b.total;
	else if (a.de != b.de)
		return a.de > b.de;
	else
		return a.id < b.id;
}
 
int main() {
	int n, low, high;
	scanf("%d %d %d", &n, &low, &high);
	vector <student > res;
	student temp;
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &temp.id, &temp.de, &temp.cai);
		if (temp.de >= low && temp.cai >= low) {
			temp.total = temp.cai + temp.de;
			if (temp.de >= high && temp.cai >= high) //德才全尽，第一梯队
				temp.level = 1;
			else if (temp.de >= high && temp.cai >= low) //德胜才，第二梯队
				temp.level = 2;
			else if (temp.de >= low && temp.cai >= low && temp.de >= temp.cai) //才德兼亡”但尚有“德胜才，第三梯队
				temp.level = 3;
			else
				temp.level = 4;
			res.push_back(temp);
		}
		
	}
	printf("%d\n", res.size());
	sort(res.begin(),res.end(), cmp);
		
	for (int j = 0; j < res.size(); j++)
		printf("%d %d %d\n", res[j].id,res[j].de, res[j].cai);
	return 0;
}
"""