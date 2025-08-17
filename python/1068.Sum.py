#https://acm.timus.ru/problem.aspx?space=1&num=1068
import sys
input =sys.stdin.readline
def solve():
	n=int(input())
	if n>0:
		print(n*(n+1)//2)
	else:
		print(1-(abs(n)*(abs(n)+1)//2))
if __name__ == "__main__":
    solve()
