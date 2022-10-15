
def epana(biggernode,j,count,niw):
    leksiko={}
    leksiko.setdefault(niw,[])
    for nodeid in biggernode[j]:
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
        xi=int(n)
        if(count%xi==0):
            niw=niw+1
    return niw
###################################
def recInter(x1low,x1high,y1low,y1high,x2low,x2high,y2low,y2high): 
      

    if(x1low > x2high or x2low > x1high): 
        return False
    if(y1high < y2low or y2high < y1low): 
        return False
   
    return True
###################################
def recIn(x1low,x1high,y1low,y1high,x2low,x2high,y2low,y2high):
    if(y2low>=y1low and y2high<=y1high and x2low>=x1low and x2high<=x1high):
        return True
    return False
#####################################
rectangles = open('data_rectangles.txt', 'r')
Result = [line.strip().split('\t') for line in rectangles.readlines()]
sorted_x = sorted(Result, key=lambda x:x[1]) # taksinomhsh kata x low
####################################
n=1024//36 # posa rectangles xoraei to node
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

niw=len(leafnode)
niwnode={}
niwnode.setdefault(niw,[])
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
    biggernode[1]=(niwnode)
    xi=int(n)
    if(count%xi==0):
        niw=niw+1

poso=len(biggernode[1])
j=1
kleidi=0

leksiko={}
niw=niw+1
count=0
oi=0
leksiko.setdefault(niw,[])
while(poso>=2):
    
    niw=epana(biggernode,j,count,niw)
    niw =niw +1
    j=j+1
    key = list(biggernode.keys())
    kleidi=kleidi+1
    if kleidi in key:
        po=key[kleidi]
    else:
        break
    if po in biggernode:
        poso=len(biggernode[po])
    else:
        poso=1

biggernode[0]=leafnode

sum=0

for dam in biggernode:
    psi=len(biggernode[dam])
    sum=sum+psi
file0 = open("StatistikaRtree.txt","w")
upsos=len(biggernode) 
file0.write("upsos\t")
file0.write("{}\n".format(upsos)) 
file0.write("nodes \t")         
file0.write("{}\n".format(sum))
count=[]
summ=[]

for height in sorted(biggernode):
    prosthesh=0
    plhthos=0
    for nodeid in biggernode[height]:
        x=len(biggernode[height][nodeid])
        plhthos=plhthos+x
        for i in range (len(biggernode[height][nodeid])):
            a1=float(biggernode[height][nodeid][i][2])
            a2=float(biggernode[height][nodeid][i][1])
            a=a1-a2
        
            b1=float(biggernode[height][nodeid][i][4])
            b2=float(biggernode[height][nodeid][i][3])
            b=b1-b2
            emvadon=a*b
            prosthesh=prosthesh+emvadon
    summ.append(prosthesh)
    count.append(plhthos)
print("plhthos")
print(count)
print("sum")
print(summ)
for i in range(len(count)):
    avg=summ[i]/count[i]
    file0.write("to plhthos ,to sum emvadon kai to avg tou epipedou \t") 
    file0.write("{}\n".format(i))
    file0.write("{}\n".format(count[i]))
    file0.write("{}\n".format(summ[i]))
    file0.write("{}\n".format(avg)) 
    file0.write("\n")

file0.close()
fileR = open("Rtree.txt","w")

rizaId =list(biggernode[upsos-1].keys())[0]
print ("riza id ")
print(rizaId)
print("\n\n")
print("upsos")
print(upsos)
print("\n\n")
fileR.write("{}\n".format(rizaId))
fileR.write("{}\n".format(upsos))
for height in sorted(biggernode):
   # fileR.write("tou epipedou \t".format(height))
   # fileR.write("{}\n".format(height))
    for nodeid in biggernode[height]:
        fileR.write("{},".format(nodeid))
        nodes=len(biggernode[height][nodeid])
        fileR.write("{},".format(nodes))
        for i in range(len(biggernode[height][nodeid])):
            fileR.write("{},".format(biggernode[height][nodeid][i]))

fileR.close()
inthat=[]
episkefthkeIN=[]
#############################################            
def RangeQueryIN(biggernode,n,tetragwno,nodeid):
    if (n!=0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recInter(tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4],biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4])):
               # print("episkefthke")
                episkefthkeIN.append(biggernode[n][nodeid][nodeid2])
                RangeQueryIN(biggernode,n-1,tetragwno,biggernode[n][nodeid][nodeid2][0])
          
    if (n==0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recIn(tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4],biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4])): 
                tetra=biggernode[n][nodeid][nodeid2]
                file2.write("{}\n".format(tetra)) 
                #print("eiani mesa sto tetragwnoxx")
                #print(tetra)
             
                inthat.append(tetra)
interr=[]
episkefthkeInter=[]              
#############################################            
def RangeQueryINT(biggernode,n,tetragwno,nodeid):
    if(n!=0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recInter(tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4],biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4])):
                
                #print("episkefthke")
                episkefthkeInter.append(biggernode[n][nodeid][nodeid2])
                RangeQueryINT(biggernode,n-1,tetragwno,biggernode[n][nodeid][nodeid2][0])
          
    if(n==0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recInter(tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4],biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4])): 
                tetra=biggernode[n][nodeid][nodeid2]
                #print("intersects")
                #print(tetra)
                file1.write("{}\n".format(tetra)) 
                interr.append(tetra)
              
outThat=[]
episkefthkeOUT=[]  
#############################################            
def RangeQueryOUT(biggernode,n,tetragwno,nodeid):
    if (n!=0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recInter(tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4],biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4])):
               # print("episkefthke")
               # print(biggernode[n][nodeid][nodeid2])
               episkefthkeOUT.append(biggernode[n][nodeid][nodeid2])
               RangeQueryOUT(biggernode,n-1,tetragwno,biggernode[n][nodeid][nodeid2][0])
          
    if (n==0):
        for nodeid2 in range(len(biggernode[n][nodeid])):
            if (recIn(biggernode[n][nodeid][nodeid2][1],biggernode[n][nodeid][nodeid2][2],biggernode[n][nodeid][nodeid2][3],biggernode[n][nodeid][nodeid2][4],tetragwno[1],tetragwno[2],tetragwno[3],tetragwno[4])): 
                tetra=biggernode[n][nodeid][nodeid2]
                #print("eiani mesa sto tetragwnoxx")
               # print(tetra)
                outThat.append(tetra)
                file3.write("{}\n".format(tetra)) 
                
###########################################
query = open('query_rectangles.txt', 'r')
queries = [line.strip().split('\t') for line in query.readlines()]


###########################################             
file1 = open("myfileIntersection.txt","w")
file2 = open("periontaiStoQ.txt","w")
file3 = open("periexounQ.txt","w")
querIN=[]
passedIN=[]

querInter=[]
passedInter=[]

querOut=[]
passedOut=[]
for tade in range (len(queries)):
    tet=queries[tade]
    
    RangeQueryINT(biggernode,upsos-1,tet,rizaId)
    querInter.append(interr)
    passedInter.append(episkefthkeInter)
    interr=[]
    episkefthkeInter=[]
    
    RangeQueryIN(biggernode,upsos-1,tet,rizaId)
    querIN.append(inthat)
    passedIN.append(episkefthkeIN)
    inthat=[]
    episkefthkeIN=[]
    
    RangeQueryOUT(biggernode,upsos-1,tet,rizaId)
    querOut.append(outThat)
    passedOut.append(episkefthkeOUT)
    outThat=[]
    episkefthkeOUT=[]
for tade in range (len(queries)):
    print("sto q"+str(tade)+"  perixontai ")
    print(len(querIN[tade]))
    print("sto q"+str(tade)+"  episkefthke ")
    print(len(passedIN[tade]))
    print("to q"+str(tade)+"  intersects ")
    print(len(querInter[tade]))
    print("to q"+str(tade)+"  episkefthke ")
    print(len(passedInter[tade]))
    print("to q"+str(tade)+"  periexetai ")
    print(len(querOut[tade]))
    print("to q"+str(tade)+"  episkefthke ")
    print(len(passedOut[tade]))
############################################## 
file1.close()   
file2.close()
file3.close()        
koma = open('myfileIntersection.txt', 'r')
koma3 = [line.strip().split('\n') for line in koma.readlines()] 
       
           
            
koma = open('periontaiStoQ.txt', 'r')
koma3 = [line.strip().split('\n') for line in koma.readlines()] 
       

koma = open('periexounQ.txt', 'r')
koma3 = [line.strip().split('\n') for line in koma.readlines()] 
       
         
            
            
            
            
            
            
