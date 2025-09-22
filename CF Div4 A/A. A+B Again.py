#https://codeforces.com/contest/1999/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n=int(input())
        print((n//10) + (n%10))
        
if __name__ == "__main__":
    solve()