#https://codeforces.com/contest/1915/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print(a ^ b ^ c)
if __name__ == "__main__":
    solve() 