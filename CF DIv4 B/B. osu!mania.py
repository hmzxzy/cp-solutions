#https://codeforces.com/contest/2009/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        lst2=[]
        for _ in range (n):
            row = input().strip()
            lst2.append(row.index("#")+1)
        print(*(lst2[::-1]))
if __name__ == "__main__":
    solve()