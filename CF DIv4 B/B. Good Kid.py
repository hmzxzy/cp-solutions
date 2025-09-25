#https://codeforces.com/contest/1873/problem/B
import sys
import math
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        max_prod = 0
        for i in range(n):
            temp = a.copy()
            temp[i] += 1
            max_prod = max(max_prod, math.prod(temp))
        print(max_prod)
if __name__ == "__main__":
    solve()
