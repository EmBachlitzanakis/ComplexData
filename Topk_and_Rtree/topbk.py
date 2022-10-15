
import sys
from heapq import heappush, heappop
Males_S = open('males_sorted', 'r')
Female_S = open('females_sorted', 'r')
############################################
###########################################       
import time
start_time = time.time()
        
#############################################  
 
number=sys.argv[1]  
number=int(number)  
kata=[]      
Q=[]       
pmale_max=0
pfemale_max=0
male_dict={}
female_dict={}
count=1
pmale_cur=0
pfemale_cur=0
condi=0
while(condi<number):
    if((count%2)!=0):   
       # Males=elenxos_m()
      #  print(Males[1])
        Males =Males_S.readline()
        Males=Males.strip().split(',')
        while(int(Males[1])<17 or Males[8][:8]==' Married' ):
            Males =Males_S.readline()
            Males=Males.strip().split(',')
        if Males[1] in male_dict:
        # append the new number to the existing array at this slot
            male_dict[Males[1]].append(Males[0])
            male_dict[Males[1]].append(Males[25])
        else:
        # create a new array in this slot
            male_dict.setdefault(Males[1],[])
            male_dict[Males[1]].append(Males[0])
            male_dict[Males[1]].append(Males[25])
        pmale_max=max(pmale_max,float(Males[25]))
        pmale_cur=float(Males[25])
    else:
        Females =Female_S.readline()
        Females=Females.strip().split(',')
        while(int(Females[1])<17 or Females[8][:8]==' Married' ):
            Females =Female_S.readline()
            Females=Females.strip().split(',')
        if Females[1] in female_dict:
        # append the new number to the existing array at this slot
            female_dict[Females[1]].append(Females[0])
            female_dict[Females[1]].append(Females[25])
        else:
        # create a new array in this slot
            female_dict.setdefault(Females[1],[])
            female_dict[Females[1]].append(Females[0])
            female_dict[Females[1]].append(Females[25])
    
        pfemale_max=max(pfemale_max,float(Females[25]))
        pfemale_cur=float(Females[25])
    
        
       
    
    T=max((pmale_max+pfemale_cur),(pfemale_max+pmale_cur))
  
    if((count%2)!=0):
        if(int(Males[1])>17 and Males[8][:8]!=' Married'):
            if Males[1] in female_dict:
                #print(Males[1])
                #print(female_dict[Males[1]])
                atoma=(len(female_dict[Males[1]]))//2
                kol=1
                for i in range (atoma):
                    j=float(Males[25])+float(female_dict[Males[1]][kol])
                    kol=kol+2
                    heappush(Q,(-1*j,Males[0]+" "+female_dict[Males[1]][i])) 
                    
    else:
        
        if(int(Females[1])>17 and Females[8][:8]!=' Married' ):
            if Females[1] in male_dict:
                atoma=len(male_dict[Females[1]])//2
                kol=1
                for i in range(atoma):
                    j=float(Females[25])+float(male_dict[Females[1]][kol])
                    kol=kol+2
                    heappush(Q,(-1*j,Females[0]+" "+male_dict[Females[1]][i])) 
                
    while Q and (Q[0][0]*(-1))>T:
        x=heappop(Q)
        print(str(x[0]*-1)+" Pair: "+x[1]) 
        kata.append(x)
    condi=len(kata)   
    count=count+1


print("--- %s seconds ---" % (time.time() - start_time))