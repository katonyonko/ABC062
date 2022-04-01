from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="062"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc074_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case


for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from heapq import heappop, heappush,heapify
  N=int(input())
  A=list(map(int,input().split()))
  h=A[:N]
  heapify(h)
  mm=[sum(h)]
  for i in range(N):
    tmp=mm[-1]
    a=heappop(h)
    b=max(a,A[N+i])
    heappush(h,b)
    mm.append(tmp-a+b)
  h=[-A[i] for i in range(2*N,3*N)]
  heapify(h)
  dd=[-sum(h)]
  for i in range(N):
    tmp=dd[-1]
    a=-heappop(h)
    b=min(a,A[2*N-i-1])
    heappush(h,-b)
    dd.append(tmp-a+b)
  dd=dd[::-1]
  print(max([mm[i]-dd[i] for i in range(N+1)]))
  """ここから上にコードを記述"""

  print(test_case[__+1])