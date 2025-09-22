#https://codeforces.com/contest/1352/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        lst=[]
        if  (n// 10000):
            lst.append(n- (n% 10000))
            n=n% 10000
        if  (n// 1000):
            lst.append(n-(n% 1000))
            n=n% 1000
        if  (n// 100):
            lst.append(n-(n% 100))
            n=n% 100
        if  (n // 10):
            lst.append(n-(n% 10))
            n=n% 10
        if n!=0:
            lst.append(n)
        print(len(lst),end="\n")
        print(*lst,end="\n")
if __name__ == "__main__":
    solve()