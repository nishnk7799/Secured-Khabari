def solution(h, q):
p=[]
for f in q:
    r=(2**h)-1
    if f>=r:
        p.append(-1)
        continue
    for i in range(h-1,0,-1):
        if r-1==f:
            p.append(r)
            break
        elif r-(2**i)==f:
            p.append(r)
            break
        elif f>r-(2**i):
            r-=1
        else:
            r-=(2**i)
return p



print(solution(3,[7,3,5,1]))