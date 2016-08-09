import math
import numpy as np
class KNN(object):
    
    def __init__(self):
        print("initialized")
        

    def fit(self,X_train,Y_train):
            self.X_train=X_train
            self.Y_train=Y_train
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
            self.t_label=t_label        

    def predict(self,X_test):
        test_id=[]
        dist=np.array([0.0,0.0,0.0])
       # t_label=self.t_label
        for i in range(len(X_test)):
              for c in range(3):
                    for z in range(len(self.t_label[c])):
                        dis=0
                        for j in range(4):
                            l1=X_test[i][j]
                            l2=self.t_label[c][z][j]
                            #print(l2,end='\t')
                            dis+=float(pow(l1-l2,2))
                        
                        if dis==0:
                            print("happened")
                        if z==0 or dis<dist[c]:
                            #print(dis)
                            dist[c]=dis
                            #point=t_label[c][z]
                            #print(dist[c])
              #print(X_test[i])
              val=min(dist)
              #print(val)
              #print(dist)
              index=[i for i in range(3) if dist[i]==val]
              #.append(X_test[i][0:4])
              #print(index)
              test_id.append(index)
              #self.t_label=t_label
        self.test_id=test_id
        return self.test_id

