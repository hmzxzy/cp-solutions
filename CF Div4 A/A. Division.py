#https://codeforces.com/contest/1669/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
       n=int(input())
       print("Division 4" if n<=1399 else("Division 3") if (1400<=n<=1599) else ("Division 2") if (1600<=n<=1899) else("Division 1"))
if __name__ == "__main__":
    solve()