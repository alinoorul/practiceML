def getAllWindows(L):
    for w in range(1, len(L)+1):
        for i in range(len(L)-w+1):
            yield L[i:i+w]
def val(arr):
    t=min(arr)
    sums=0
    for i in arr:
        sums+=i
    return sums*t 
    
def greatestValueDays(ratings):
    L=ratings
    p  = [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]

    maxr=None
    for r in p:
        if maxr is None:
            maxr=r
        elif val(maxr)<val(r):
            maxr=r
    return val(maxr)
        
    maxindex = ratings.index(max(ratings))
    for i in range(len(ratings)):
        rlen=i+1
        r=[]
        for i in range(rlen):
            if(maxindex>=0 and maxindex<=len(ratings)-1):
                s=[ratings[maxindex:maxindex+i+1],ratings[maxindex-i:maxindex+1]]
                s1=sum(s[0])
                s2=sum(s[1])
                if(s1>s2):
                    r=ratings[maxindex:maxindex+i+1]
                else:
                    r=ratings[maxindex-i:maxindex+1]
        if maxr is None:
            maxr=r
        elif val(maxr)<val(r):
            maxr=r
        else:
            break
    return val(maxr)
ratings = [3,1,6,4,5,2]
print(greatestValueDays(ratings))