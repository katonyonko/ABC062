from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="062"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc074_a".format(times, problem)) as res:
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
  H,W=map(int,input().split())
  ans=H*W
  for i in range(H+1):
    tmp=[i*W,(H-i)//2*W,(H-i+1)//2*W]
    ans=min(ans,max(tmp)-min(tmp))
    tmp=[i*W,W//2*(H-i),(W+1)//2*(H-i)]
    ans=min(ans,max(tmp)-min(tmp))
  for j in range(W+1):
    tmp=[j*H,(W-j)//2*H,(W-j+1)//2*H]
    ans=min(ans,max(tmp)-min(tmp))
    tmp=[j*H,H//2*(W-j),(H+1)//2*(W-j)]
    ans=min(ans,max(tmp)-min(tmp))
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])