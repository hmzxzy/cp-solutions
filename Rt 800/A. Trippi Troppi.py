#https://codeforces.com/contest/2094/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        p1,p2,p3 = map(str,input().split())
        print(p1[0]+p2[0]+p3[0])
        
if __name__ == "__main__":
    solve()