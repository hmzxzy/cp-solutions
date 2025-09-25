#https://codeforces.com/contest/1915/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        row1=input().strip()
        row2=input().strip()
        row3=input().strip()
        concat=row1+row2+row3
        ca=concat.count("A")
        cb=concat.count("B")
        cc=concat.count("C")
        if ca!=3 :
            print("A")
        if cb!=3 :
            print("B")
        if cc!=3 :
            print("C")
if __name__ == "__main__":
    solve()