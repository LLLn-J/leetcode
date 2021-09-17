
nums= [1,2,3,1]
s=set()
for n in nums:
    if n in s:
        print("true")
        break
    else:
        s.add(n)
print("false")