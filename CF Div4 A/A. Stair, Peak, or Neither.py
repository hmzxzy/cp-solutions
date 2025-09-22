#https://codeforces.com/contest/1950/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print("STAIR") if a<b<c else print("PEAK") if b>a and b>c else print("NONE")
        
if __name__ == "__main__":
    solve()