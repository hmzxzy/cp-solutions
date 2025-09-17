#https://codeforces.com/contest/1926/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        a = s.count("A")
        b = s.count("B")
        print("A") if a>b else print("B")
if __name__ == "__main__":
    solve() 