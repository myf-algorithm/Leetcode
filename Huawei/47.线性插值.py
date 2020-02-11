"""
#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
    int m, n;
    while (cin >> m >> n)
    {
        int M, N, A, B;
        cin >> M >> A;
        cout << M << " " << A << endl;
        for (int i = 1; i < m; ++i)
        {
            cin >> N >> B;
            if (N == M) continue; // 重复数据，丢弃
            else
            {
                // 不连续，在M-N之间插值
                for (int j = 1; j < N - M; ++j)
                {
                    cout << M + j << " " << A + ((B - A) / (N - M))*j << endl;
                }
                cout << N << " " << B << endl;
                M = N;
                A = B;
            }
        }
    }
    return 0;
}
"""
