import io
import sys

_INPUT = """\
6
3 10
-2 8 -5
5 -10 3
5 -1
10 -20 30 -40 50
-10 20 -30 40 -50
1 100
30
60
4 865942261
703164879 -531670946 -874856231 -700164975
-941120316 599462305 -649785130 665402307
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  Y=list(map(int,input().split()))
  Z=list(map(int,input().split()))
  pos,neg=[(0,-1,1)],[(0,-1,1)]
  for i in range(N):
    if Y[i]>0: pos.append((Y[i],i,0))
    else: neg.append((Y[i],i,0))
    if Z[i]>0: pos.append((Z[i],i,1))
    else: neg.append((Z[i],i,1))
  if X>0: pos.append((X,-1,2))
  else: neg.append((X,-1,2))
  pos.sort()
  neg.sort(key=lambda x: -x[0])
  dp=[10**20]*(len(pos)*len(neg)*2)
  dp[0]=0
  dp[1]=0
  s=set()
  for i in range(len(pos)):
    if i>0 and pos[i][2]==1: s.add(pos[i][1])
    tmp=s.copy()
    for j in range(len(neg)):
      if j>0 and neg[j][2]==1: tmp.add(neg[j][1])
      if i<len(pos)-1:
        if pos[i+1][2]>0 or pos[i+1][2]==0 and pos[i+1][1] in tmp:
          dp[(i+1)*len(neg)*2+j*2]=min(dp[(i+1)*len(neg)*2+j*2],dp[i*len(neg)*2+j*2]+abs(pos[i][0]-pos[i+1][0]))
          dp[(i+1)*len(neg)*2+j*2+1]=min(dp[(i+1)*len(neg)*2+j*2+1],dp[i*len(neg)*2+j*2]+abs(pos[i][0]-pos[i+1][0])+abs(pos[i+1][0]-neg[j][0]))
      if j<len(neg)-1:
        if neg[j+1][2]>0 or neg[j+1][2]==0 and neg[j+1][1] in tmp:
          dp[i*len(neg)*2+(j+1)*2+1]=min(dp[i*len(neg)*2+(j+1)*2+1],dp[i*len(neg)*2+j*2+1]+abs(neg[j][0]-neg[j+1][0]))
          dp[i*len(neg)*2+(j+1)*2]=min(dp[i*len(neg)*2+(j+1)*2],dp[i*len(neg)*2+j*2+1]+abs(neg[j][0]-neg[j+1][0])+abs(neg[j+1][0]-pos[i][0]))
  if X>0:
    idx=pos.index((X,-1,2))
    ans=min([dp[idx*len(neg)*2+j*2] for j in range(len(neg))])
  else:
    idx=neg.index((X,-1,2))
    ans=min([dp[i*len(neg)*2+idx*2+1] for i in range(len(pos))])
  print(-1 if ans==10**20 else ans)