import io
import sys

_INPUT = """\
6
2
3
0
10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def f(x):
    if x==0: return 1
    res=x*f(x-1)
    return res
  N=int(input())
  print(f(N))