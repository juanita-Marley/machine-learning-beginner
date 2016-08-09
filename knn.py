#from sklearn import datasets
from math import pow
import numpy as np
#from sklearn.cross_validation import train_test_split as spl
#iris=datasets.load_iris()
#X=iris.data
#Y=iris.target
#X_train, X_test,Y_train, Y_test=spl(X,Y,test_size=0.5)



def ddisplay(data_display):
    print("new print")
    for x in range(len(data_display)):
        for j in range(4):
            print(data_display[x][j],end="\t")
        print(' ')

def fit(X_train,Y_train):
        type0=[]
        type1=[]
        type2=[]
        t_label=[type0,type1,type2]
        for i in range(len(Y_train)):
            if Y_train[i]==1:
                type1.append(X_train[i][0:4])
            elif Y_train[i]==0:
                type0.append(X_train[i][0:4])
            else:
                type2.append(X_train[i][0:4])
            
#test_id=np.zeros(len(X_test))

#fit(X_train,Y_train)
#print(X_train)
#[ddisplay(t_label[j]) for j in range(3)] # displays data according to labels
#dist=np.array([0.0,0.0,0.0])
#print(t_label[0][0][0])
def predict(X_test):
    test_id=[]
    for i in range(len(X_test)):
          for c in range(3):
                for z in range(len(t_label[c])):
                    dis=0
                    for j in range(4):
                        l1=X_test[i][j]
                        l2=t_label[c][z][j]
                        #print(l2,end='\t')
                        dis+=float(pow(l1-l2,2))
                    
                    if dis==0:
                        print("happened")
                    if z==0 or dis<dist[c]:
                        #print(dis)
                        dist[c]=dis
                        point=t_label[c][z]
                        #print(dist[c])
          #print(X_test[i])
          val=min(dist)
          #print(val)
          #print(dist)
          index=[i for i in range(3) if dist[i]==val]
          #print(index)
          test_id.append(index)
    return test_id          
          
          
#nearest_neighbour(X_test)
#print(test_id,end='\t')
#print(Y_test)


    # 5.1 3.8 1.6 0.2    5.7 2.5 5 2    6.3 2.5 5 1.9
    # 6.3 2.9 5.6 1.8     


     
        
