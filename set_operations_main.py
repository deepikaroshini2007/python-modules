import setmodule
s1=set(map(int,input(&quot;Enter the elements of set1:&quot;).split()))
s2=set(map(int,input(&quot;Enter the elements of set2:&quot;).split()))
uni=setmodule.sunion(s1,s2)
print(&quot;Union :&quot;,uni)
inter=setmodule.sintersection(s1,s2)
print(&quot;Intersection :&quot;,inter)
diff=setmodule.sdifference(s1,s2)
print(&quot;Difference :&quot;,diff)

sdiff=setmodule.ssymmetricdiff(s1,s2)
print(&quot;Symmetric Difference :&quot;,sdiff)
