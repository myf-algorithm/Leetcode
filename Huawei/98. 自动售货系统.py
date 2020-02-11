"""
#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <stdlib.h>
using namespace std;
vector<int> pt1={0,0,0,0,0,0},pt2={2,3,4,5,8,6};
vector<vector<int>> goods;//商品数量及价格
vector<int> coin={0,0,0,0};//一元，两元，五元，十元零钱数量
vector<int> yuan={1,2,5,10};
int pay=0;//投币金额
bool Initialization(string comd)
{
    char c;
    int i,j;
    pay=0;
    j=comd.find(';');
    comd=comd.substr(2,j-2);
    j=comd.find(' ');
    string s1,s2;
    s1=comd.substr(0,j);
    s2=comd.substr(j+1);
    for(i=0,j=0;i<s1.size();i++)
    {
        if(isdigit(s1[i]))
        {
            if(i+1<s1.size() && isdigit(s1[i+1]))
            {
                string temp=s1.substr(i,2);
                goods[0][j]=atoi(temp.c_str());
                j++;
                i++;
            }else{
                goods[0][j]=s1[i]-48;
                j++;
            }
        }
    }
    for(i=0,j=0;i<s2.size();i++)
    {
        if(isdigit(s2[i]))
        {
            if(i+1<s2.size() && isdigit(s2[i+1]))
            {
                string temp=s2.substr(i,2);
                coin[j]=atoi(temp.c_str());
                j++;
                i++;
            }else{
                coin[j]=s2[i]-48;
                j++;
            }
        }
    }
    cout<<"S001:Initialization is successful"<<endl;
    return true;
}
int CheckPay(string comd)
{
    int p1,j;
    j=comd.find(';');
    comd=comd.substr(2,j-2);
    p1=atoi(comd.c_str());
    if(p1!=1 && p1!=2 && p1!=5 && p1!=10)
    {
        cout<<"E002:Denomination error"<<endl;
        return -2;
    }else if(p1 > coin[0]+2*coin[1])
    {
        cout<<"E003:Change is not enough, pay fail"<<endl;
        return -3;
    }else if(p1>10)
    {
        cout<<"E004:Pay the balance is beyond the scope biggest"<<endl;
        return -4;
    }else if(accumulate(goods[0].begin(),goods[0].end(),0)==0)
    {
        cout<<"E005:All the goods sold out"<<endl;
        return -5;
    }else
    {
        pay+=p1;
        cout<<"S002:Pay success,balance="<<pay<<endl;//当前金额？总金额？
        if(p1==1) coin[0]++;
        else if(p1==2) coin[1]++;
        else if(p1==5) coin[2]++;
        else if(p1==10) coin[3]++;
        return 1;
    }
}
int Buy(string comd)
{
    int j;
    j=comd.find(';');
    string name=comd.substr(2,j-2);
    if(name!="A1" && name!="A2" && name!="A3" && name!="A4" && name!="A5" && name!="A6")
    {
        cout<<"E006:Goods does not exist"<<endl;
        return -6;
    }
    if(goods[0][name[1]-49]==0)
    {
        cout<<"E007:The goods sold out"<<endl;
        return -7;
    }
    if(goods[1][name[1]-49]>pay)
    {
        cout<<"E008:Lack of balance"<<endl;
        return -8;
    }
    pay-=goods[1][name[1]-49];
    goods[0][name[1]-49]--;
    cout<<"S003:Buy success,balance="<<pay<<endl;
    return 1;
}
bool CoinReturn()
{
    vector<int> ret={0,0,0,0};
    if(pay==0)
    {
        cout<<"E009:Work failure";
        return false;
    }
    int i;
    for(i=3;pay!=0 && i>=0; )
    {
        if(pay>=yuan[i] && coin[i]>0)
        {
            pay-=yuan[i];
            coin[i]--;
            ret[i]++;
        }else i--;
    }
    for(i=0;i<4;i++)
        cout<<yuan[i]<<" yuan coin number="<<ret[i]<<endl;
    return true;
}
void Query(string comd)
{
    int num,i;
    i=comd.find(';');
    comd=comd.substr(2,i-2);
    if(comd.size()!=1)
        num=-1;
    else
        num=comd[0]-48;
    if(num==0)
        for(i=0;i<6;i++)
            cout<<'A'<<i+1<<' '<<goods[1][i]<<' '<<goods[0][i]<<endl;
    else if(num==1)
        for(i=0;i<4;i++)
            cout<<yuan[i]<<" yuan coin number="<<coin[i]<<endl;
    else
        cout<<"E010:Parameter error";
}
int main()
{
    string command;
    goods.push_back(pt1);goods.push_back(pt2);
    while(getline(cin,command))
    {
        for(int i=0;i<command.size();i++)
        {
            if(command[i]=='r') Initialization(command.substr(i));
            else if(command[i]=='p') CheckPay(command.substr(i));
            else if(command[i]=='b') Buy(command.substr(i));
            else if(command[i]=='c') CoinReturn();
            else if(command[i]=='q') Query(command.substr(i));
        }
    }
    return 0;
}
"""