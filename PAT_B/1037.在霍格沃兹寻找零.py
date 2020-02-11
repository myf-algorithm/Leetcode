P, A = list(map(str, input().strip().split()))
P_Galleon, P_Sickle, P_Knut = list(map(int,  P.split('.')))
A_Galleon, A_Sickle, A_Knut = list(map(int,  A.split('.')))
P_sum = P_Galleon * 17 * 29 + P_Sickle * 29 + P_Knut
A_sum = A_Galleon * 17 * 29 + A_Sickle * 29 + A_Knut
if P_sum <= A_sum:
    Knut_A = A_sum - P_sum
    print("%d.%d.%d" %(Knut_A / (17 * 29), Knut_A % (17 * 29) /29, Knut_A % 29))
else:
    Knut_A = P_sum - A_sum
    print("-%d.%d.%d" %(Knut_A / (17 * 29), Knut_A % (17 * 29) /29, Knut_A % 29))