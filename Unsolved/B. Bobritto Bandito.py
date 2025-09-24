#https://codeforces.com/contest/2094/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n, m, l,r = map(int, input().split())
        print(f"{l} {m+l-1}")
if __name__ == "__main__":
    solve()