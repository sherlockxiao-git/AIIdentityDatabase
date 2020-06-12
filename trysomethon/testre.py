import re
# s1="E:\AIChangingFace\iddatabase\\14.jpg"
# c1=int(re.search(r"\d+",s1)[0])
c1=()
c1=(("2","12"),)
# c1="".join(c1[0])
c1=c1[0]
# s1=' '.join([c1 for str(i) in c1])
s1=[str(i) for i in c1]

# c1=",".join(c1)
print(",".join(s1))