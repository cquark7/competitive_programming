#include <stdio.h>
#include <string.h>
const int Mod = 1e9 + 7;
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
int vals[100][150][150] = {0}, prev[100][150][150] = {0};
int main()
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        memset(vals, 0, sizeof(vals));
        memset(prev, 0, sizeof(prev));
        int n, n2, i, j, k, m, mx, nmx, ans=0, a[100]={0};
        scanf("%d", &n);
        for(i=1; i<=n; i++) scanf("%d", &a[i]);
        n2 = n;
        if (n < 2){
            printf("1\n"); continue;}
        vals[2][a[1]][a[2]] = 1;
        prev[2][a[1]][a[2]] = 1;
        mx = MAX(a[1], a[2]);
        for (i=2; i<=n2; i++)
        {
            nmx = mx;
            for(j=0; j<=mx; j++)
                for(k=0; k<=mx; k++){
                    if(prev[i][j][k]){
                        if ((i > n && k > 0) || i == n)
                            ans = (ans + vals[i][j][k]) % Mod;
                        for(m=0; m<=MIN(j, k); m++){
                            vals[i + 1][k - m][a[i + 1] + m] = (vals[i + 1][k - m][a[i + 1] + m] + vals[i][j][k])%Mod;
                            prev[i + 1][k - m][a[i + 1] + m] = 1;
                        }
                        nmx = MAX(nmx, a[i + 1] + MIN(j, k));
                        if (j*k > 0)
                            n2 = MAX(n2, i+1);
                    }

                }
            mx = nmx;
        }
        printf("%d\n", ans);
    }
    return 0;
}
