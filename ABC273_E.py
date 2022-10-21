import io
import sys

_INPUT = """\
6
11
ADD 3
SAVE 1
ADD 4
SAVE 2
LOAD 1
DELETE
DELETE
LOAD 2
SAVE 1
LOAD 3
LOAD 1
21
ADD 4
ADD 3
DELETE
ADD 10
LOAD 7
SAVE 5
SAVE 5
ADD 4
ADD 4
ADD 5
SAVE 5
ADD 2
DELETE
ADD 1
SAVE 5
ADD 7
ADD 8
DELETE
ADD 4
DELETE
LOAD 5
7
ADD 2
ADD 3
SAVE 1
LOAD 1
LOAD 2
SAVE 3
LOAD 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Q=int(input())
  parent={}
  now=0
  cnt=1
  d={}
  dd={}
  G=[set()]
  G2=[-1]
  ans=[]
  for i in range(Q):
    query=input().split()
    if query[0]=='ADD':
      x=int(query[1])
      if x in G[now]:
        now=d[(now,x)]
      else:
        G[now].add(x)
        G.append(set())
        G2.append(x)
        d[(now,x)]=cnt
        parent[cnt]=now
        now=cnt
        cnt+=1
    elif query[0]=='DELETE':
      if now!=0: now=parent[now]
    elif query[0]=='SAVE':
      y=int(query[1])
      dd[y]=now
    else:
      z=int(query[1])
      if z in dd: now=dd[z]
      else: now=0
    ans.append(G2[now])
  print(*ans)