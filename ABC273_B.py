import io
import sys

_INPUT = """\
6
2048 2
1 15
999 3
314159265358979 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,K=map(int,input().split())
  for i in range(K):
    X=X//(10**(i+1))*(10**(i+1)) if X%(10**(i+1))//(10**i)<=4 else (X//(10**(i+1))+1)*(10**(i+1))
  print(X)