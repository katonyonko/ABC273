import io
import sys

_INPUT = """\
6
5 5 4 4
3
5 3
2 2
1 4
4
L 2
U 3
L 2
R 4
6 6 6 3
7
3 1
4 3
2 6
3 4
5 5
1 1
3 2
10
D 3
U 3
L 2
D 2
U 3
D 3
U 3
R 3
L 3
D 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  from collections import defaultdict
  H,W,rs,cs=map(int,input().split())
  N=int(input())
  dr,dc=defaultdict(list),defaultdict(list)
  for i in range(N):
    r,c=map(int,input().split())
    dr[r].append(c)
    dc[c].append(r)
  for r in dr: dr[r].sort()
  for c in dc: dc[c].sort()
  Q=int(input())
  for i in range(Q):
    d,l=input().split()
    l=int(l)
    if d=='U' or d=='D':
      if cs in dc:
        x=bisect_left(dc[cs],rs)
        if d=='U':
          if x==0: rs-=min(l,rs-1)
          else:
            rs-=min(l,rs-1-dc[cs][x-1])
        else:
          if x==len(dc[cs]): rs+=min(l,H-rs)
          else: rs+=min(l,dc[cs][x]-rs-1)
      else:
        if d=='U': rs-=min(l,rs-1)
        else: rs+=min(l,H-rs)
    else:
      if rs in dr:
        x=bisect_left(dr[rs],cs)
        if d=='L':
          if x==0: cs-=min(l,cs-1)
          else: cs-=min(l,cs-1-dr[rs][x-1])
        else:
          if x==len(dr[rs]): cs+=min(l,W-cs)
          else: cs+=min(l,dr[rs][x]-cs-1)
      else:
        if d=='L': cs-=min(l,cs-1)
        else: cs+=min(l,W-cs)
    print(rs,cs)