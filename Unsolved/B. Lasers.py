#https://codeforces.com/contest/2148/problem/B
#tricky problem ;)
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(n+m)
if __name__ == "__main__":
    solve()
