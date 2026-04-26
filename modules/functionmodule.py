def factors(n):
l=[]
for i in range(1,n+1):
if n%i==0:
l.append(i)
return l
def primeFactors(n):
l=[]
i=2
while i&lt;=n:
if n%i==0:
l.append(i)
n=n//i
else:
i+=1
return l
