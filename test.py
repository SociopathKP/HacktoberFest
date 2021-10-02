n=int(input())
l=list(map(int,input().split()))

if(sum(l)==n):
  print("Special")
else:
  print("Fake")
