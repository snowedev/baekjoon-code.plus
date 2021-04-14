# 포도주 시식 # B_2156
# 이친수와 비슷
"""
* 2차원 풀이
 D[i][j] = A[1] ~ A[i]가 있을 때 포도주를 마신 최댓값, j는 3이상이 될 수 없다
 j = 연속으로 마신 횟수
 j=0 -> i번째 포도주를 안마심
 (D[i][0] = max(D[i-1][0], D[i-1][1], D[i-1][2]) )
 j=1 -> i번째 마심, 연속 1
 (D[i][1] = D[i-1][0]+A[i])
 j=2 -> i번째 마심, 연속 2
 (D[i][0] = D[i-1][1]+A[i])

* 1차원 풀이
D[i] = i 번째까지의 최대 양
1. i 번째를 마시지 않은 경우 : D[i-1]
2. i 번째를 마신경우 - 1번 연속 : D[i-2] + A[i]
3. i 번째를 마신경우 - 2번 연속 : D[i-3] + A[i-1] + A[i]
"""
n = int(input())
a = [0] + [int(input()) for _ in range(n)]
d = [0] * (n+1)
d[1] = a[1]

if n >= 2:
    d[2] = a[1] + a[2]

for i in range(3, n+1):
    d[i] = d[i-1]
    d[i] = max(d[i], d[i-2]+a[i])
    d[i] = max(d[i], d[i-3]+a[i-1]+a[i])

print(d[n])
