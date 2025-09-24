#https://codeforces.com/contest/2044/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a = input().strip()
        i = 0
        b= ""
        while i < len(a):
            if a [i] == "p":
                b = b+ "q"
                i+=1
            elif a[i] == "q":
                b = b+ "p"
                i+=1
            else :
                b = b+a[i]
                i+=1
        print(b[::-1])
if __name__ == "__main__":
    solve()