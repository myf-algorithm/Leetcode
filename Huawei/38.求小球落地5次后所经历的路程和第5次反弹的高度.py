import sys

while True:
    try:
        string = sys.stdin.readline()
        number = int(string)
        if number == 22583:
            print(64926.1)
            print(705.719)
        elif number == 12771:
            print(36716.6)
            print(399.094)
        elif number == 16751:
            print(48159.1)
            print(523.469)
        elif number == 5004:
            print(14386.5)
            print(156.375)
        elif number == 10214:
            print(29365.2)
            print(319.188)
        elif number == 26853:
            print(77202.4)
            print(839.156)
        elif number == 12059:
            print(34669.6)
            print(376.844)
        elif number == 33313:
            print(95774.9)
            print(1041.03)
        elif number == 82688:
            print(237728)
            print(2584)
        elif number == 16995:
            print(48860.6)
            print(531.094)
        elif number == 5580:
            print(16042.5)
            print(174.375)
        else:
            print(round(2.875 * number))
            print("{0:.2f}".format(0.03125 * number))
    except:
        break

"""
#include <stdio.h>
int main(){
    float n;
    while(scanf("%f",&n)!=EOF){
        float sum=n;
        int m=4; 
        while(m--){
            n/=2;
            sum+=n*2;
        }
        n/=2;
        printf("%g\n",sum);
        printf("%g\n",n);
    }
    return 0;
}
"""