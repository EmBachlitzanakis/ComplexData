def epana(biggernode,j,count,niw):
    leksiko={}
    leksiko.setdefault(niw,[])
    xik=biggernode[j].keys()
    for nodeid in xik:
        xlow=[]
        xhigh=[]
        ylow=[]
        yhigh=[]
        lis=[]
        for i in range (len(biggernode[j][nodeid])):
            xlow.append(biggernode[j][nodeid][i][1])     
            xhigh.append(biggernode[j][nodeid][i][2])
            ylow.append(biggernode[j][nodeid][i][3])
            yhigh.append(biggernode[j][nodeid][i][4])
        ptr=nodeid
        lis.append(ptr)
        count=count+1
        xilow=min(xlow)
        lis.append(xilow)
        xihigh=max(xhigh)
        lis.append(xihigh)
        yilow=min(ylow)
        lis.append(yilow)
        yihigh=max(yhigh)
        lis.append(yihigh)
        leksiko.setdefault(niw,[]).append(lis)
    
        oi=j+1
   
        biggernode[oi]=(leksiko)
        if(count%n==0):
            niw=niw+1







###################################
rectangles = open('data_rectangles.txt', 'r')
Result = [line.split('\t') for line in rectangles.readlines()]

sorted_x = sorted(Result, key=lambda x:x[1]) # taksinomhsh kata x low
#print(sorted_x[:2])

####################################
#print(len(Result))
n=1024//36 # posa rectangles xoraei to node
#print(n)
p=len(Result)//n #number of leaf level pages
ifaker=(len(Result)%n)
if (ifaker!=0):
    p=p+1
d=p**(1/2) #S vertical slices
S =int(d)

#####################################
slic=S*n
node=[]

nodeid=0
leafnode={}
leafnode.setdefault(nodeid,[])
lis=[]
count=0
i=1
while(len(sorted_x)>0):
    sorted_y=sorted(sorted_x[:slic],key=lambda x:x[3])  
    littlenode=[] 
    for i in range(S):  
        xi=sorted_y[:n]
        for j in xi:
            littlenode=j
            leafnode.setdefault(nodeid,[]).append(littlenode)
        del sorted_y[:n]
        nodeid=nodeid+1
    del sorted_x[:slic]

niw=len(leafnode)+1
niwnode={}
niwnode.setdefault(niw,[])
nrw=0
biggernode={}
for nodeid in leafnode:
    xlow=[]
    xhigh=[]
    ylow=[]
    yhigh=[]
    lis=[]
        
    for i in range (len(leafnode[nodeid])):
        xlow.append(leafnode[nodeid][i][1])     
        xhigh.append(leafnode[nodeid][i][2])
        ylow.append(leafnode[nodeid][i][3])
        yhigh.append(leafnode[nodeid][i][4])
    ptr=nodeid
    lis.append(ptr)
    count=count+1    
    
    xilow=min(xlow)
    lis.append(xilow)
    xihigh=max(xhigh)
    lis.append(xihigh)
    yilow=min(ylow)
    lis.append(yilow)
    yihigh=max(yhigh)
    lis.append(yihigh)
    niwnode.setdefault(niw,[]).append(lis)
    biggernode[nrw]=(niwnode)
    if(count%n==0):
        niw=niw+1
poso=len(biggernode[0])
j=0
kleidi=0

leksiko={}
niw=niw+1
count=0
oi=0
leksiko.setdefault(niw,[])
while(poso>=2):
    epana(biggernode,j,count,niw)

    j=j+1
    #print(j)
    key = list(biggernode.keys())
    kleidi=kleidi+1
    if kleidi in key:
        po=key[kleidi]
    else:
        break
    #print(po)
    if po in biggernode:
        poso=len(biggernode[po])
        #print(poso)
    else:
        poso=1
   # print(biggernode[j])
#key = list(biggernode.keys())
#print(key)
#print(biggernode[0][5][1][1])
#print(len(biggernode))
#print(len(leafnode))

sum=len(leafnode)

for dam in biggernode:
    psi=len(biggernode[dam])
    sum=sum+psi
print(sum)            
print(len(biggernode))
#print(niwnode)
#print(len(leafnode))



