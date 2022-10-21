import io
import sys

_INPUT = """\
6
6
2 7 1 8 2 8
1
1
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import Counter
  N=int(input())
  A=list(map(int,input().split()))
  S=set(A)
  n=len(S)
  c=Counter(A)
  d=sorted([k for k in c])
  ans=[0]*N
  for i in range(len(d)):
    n-=1
    ans[n]=c[d[i]]
  print(*ans,sep='\n')