 #called to use data from heartdata.txt file
# pre-process  data
import numpy as np
import math
class heartdata(object):
    
    def __init__(self):
        self.size="303 * 14"  
        f=open("heartdata.txt",'r')
        str1='1'
        li=[]   # 303 * 14 items index max is 302 * 13
        label=[]
        c=1
        while  len(str1)>0:
            str1=f.readline()
            if c in [88,167,193,267,288,303]:
                pass
            else:
                li.append(str1.split(','))
            c+=1
        f.close()
        self.li=li
        [label.append(int(li[i][13])) for i in range(297)]
        self.label=label

        Dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
        D={0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{},11:{},12:{}}
        for j in range(13):
            for i in range(297):
                if li[i][j]  in Dict[j]:
                    x=li[i][j]
                    v=str(x)
                    D[j][v][0]+=1
                    
                else:
                    Dict[j].append(li[i][j])
                    x=li[i][j]
                    v=str(x)
                    D[j][v]=[0]
                    
                    
        self.Dict=Dict
        self.D=D
        
    def TotalE(self):   
        C=np.zeros(2)
        ET=0
        for i in range(297):
            if self.label[i]==0:
                C[0]+=1
            else:
                self.label[i]=1
                C[1]+=1
        sumT=C[1]+C[0]
        for j in range(2):
            x=C[j]/sumT
            ET-=x*math.log2(x)             
        self.ET=ET
        
   
    def entropy(self,Anum,x):
        cv=np.zeros(2)
        for j in range(2):
            for k in range(297):
                if self.li[k][Anum]==x:
                    cv[j]+=1
                  
        
        sum0=0  
        E=0
        sum0=sum([cv[j] for j in range(2)]) 
        for j in range(2):
            x=cv[j]/sum0
            E-=x*math.log2(x)
        return E    
        
            
    def gain(self):
        Gainhigh=0
        for Anum in range(13):
            I=self.Dict[Anum] # Dict is a dictionary 
            y=sum([self.D[Anum][str(c)][0]* self.entropy(Anum,c)/297  for c in I])
            G=self.ET-y
            print(G)
            if  Gainhigh<G and Anum in [1,2,5,6,8,10,11,12] :
                Gainhigh=G
                A=Anum
        self.A=A


    def gain2(self):
               
            j=self.Dict[11][3]
            print(j)
            Gainhigh=0
            for Anum in range(13):
                l=len(self.Dict[Anum])
                
                sumTot=0
                E=0
                
                if Anum in [1,2,5,6,8,10,12]:
                    for c in range(l):
                            cv=np.zeros(2)
                            sumT=0
                            ET=0
                            for i in range(297):
                                #print(self.li[i][11])
                                #print(self.li[i][Anum],end='\t')
                                #print(self.Dict[Anum][c])
                                if (self.li[i][11]==j and self.li[i][Anum]==self.Dict[Anum][c]) :
                                    #print(self.li[i][11])
                                    #print(self.li[i][Anum])
                                    #print(self.Dict[Anum][c])
                                    if self.label[i]==0:
                                        cv[0]+=1
                                    else:
                                        cv[1]+=1
                                        
                            if cv[0]==0 or cv[1]==0:
                                print("reaches")
                                print(cv[0],   cv[1])
                            #print(sumT)
                            else:
                                sumT=cv[1]+cv[0]
                                for k in range(2):
                                    x=cv[k]/sumT
                                    ET-=x*math.log2(x)
                                sumTot+=sumT
                                E+=sumT*ET
                    G=self.ET-(E/sumTot)
                    print(G)
                    if G>Gainhigh:
                        Gainhigh=G
                        A=Anum
            print(A)                                            

                     
       
        




        









                           
