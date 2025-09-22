#https://codeforces.com/contest/1760/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print(b) if(a<b<c or c<b<a) else print(c) if (a<c<b or b<c<a) else print(a)
if __name__ == "__main__":
    solve() 