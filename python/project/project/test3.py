import os
import numpy as np
import math
os.system('cls')

def movielist ():
    
    movie_file = open('Movies.txt')
    readM = movie_file.readlines()
    for line in readM:
        for item in line:
            for char in item :
                if char=='\t':
                    print('\t',end ='') 
                elif char=='\n':

                    print('\n', end='')
                    print('\n', end='')
                else:
                    print(char, end='')

def comments ():
    Rating_file = open('Ratings.txt')
    readR = Rating_file.readlines()
    # print(readR)
    for line in readR:
        for item in line:
            for char in item :
                if char=='\t':
                    print('\t',end ='') 
                elif char=='\n':

                    print('\n', end='')
                    print('\n', end='')
                else:
                    print(char, end='')
                    
                    
def sim(target1,target2):
    Rating_file = open('Ratings.txt')
    readR = Rating_file.readlines()
    ranked =[]
    ranked2 =[]
    sim=np.array
    counter=0
    multi=0
    x=0
    ratings1=[]
    ratings2=[]
    # print(readR)1
    for item in readR:
        
        part = item.strip().split('\t')
        # print(part[0])
        if part[0]==target1:
            # print("okay")
            ranked.append([int(part[1]),int(part[2])])
        if part[0]==target2:
        # print("okay")
            ranked2.append([int(part[1]),int(part[2])])
    f_matrix=np.array(ranked)
    s_matrix=np.array(ranked2)
    # frow=f_matrix[:,0]
    # frrow=f_matrix[:,1]
    
    for i in range(s_matrix.shape[0]):
        srow=s_matrix[i][0]
        srrow=s_matrix[i][1]
        multi=0
        for j in range(f_matrix.shape[0]):
            
            if f_matrix[j][0]==srow:
                
                counter+=1
                frrow=f_matrix[j][1]
                multi=srrow*frrow
                x+=multi
                ratings1.append(frrow)
                ratings2.append(srrow)
                
                print(srow)
    sqrr = [x**2 for x in ratings1]
    sqrr2 = [x**2 for x in ratings2]
    
    t1= sum(sqrr)
    t2= sum(sqrr2)
 
    # print(x)
    y=np.sqrt(t1)
    z=np.sqrt(t2)
    g=z*y
    if g==0:
        res=0
    else :
        res = x/g
            
            
    return res
       #dsfdsfdsfdsfdsf     
    
    
def recomandation(target):
    x=[]
    for i in range(51 ):
        print(i)
        print(target)
        y=sim(str(target),str(i))
        print(y)
        x.append((y,i))
    x.sort(reverse=True)
    print(x)
    print("x : ",x[1])
    s,u=x[1]
    
    Rating_file = open('Ratings.txt')
    readR = Rating_file.readlines()
    ranked =[]
    ranked2 =[]
    sim=np.array
    counter=0
    multi=0
    x=0
    ratings1=[]
    ratings2=[]
    # print(readR)1
    for item in readR:
        
        part = item.strip().split('\t')
        # print(part[0])
        if part[0]==target:
            # print("okay")
            ranked.append([int(part[1]),int(part[2])])
        if part[0]==u:
        # print("okay")
            ranked2.append([int(part[1]),int(part[2])])
    f_matrix=np.array(ranked)
    s_matrix=np.array(ranked2)
    # frow=f_matrix[:,0]
    # frrow=f_matrix[:,1]
    
    for i in range(s_matrix.shape[0]):
        srow=s_matrix[i][0]
        srrow=s_matrix[i][1]
        multi=0
        for j in range(f_matrix.shape[0]):
            
            if srow=if_matrix[j][0]:
                
                counter+=1
                frrow=f_matrix[j][1]
                multi=srrow*frrow
                x+=multi
                ratings1.append(frrow)
                ratings2.append(srrow)
   
            
        
    

while True :
    
                    
    inpot =int(input("press what you want to do :"))

    if inpot==1 :
        os.system('cls')
        movielist()
        print('\n')
        # inpot =int(input("press what you want to do :"))
    elif inpot==2:
        os.system('cls')
        comments()
        print('\n')
        # inpot =int(input("press what you want to do :"))
    elif inpot==0:
        print('\n')
        os.system('cls')
        # inpot =int(input("press what you want to do :"))
    elif inpot==3:
        print('\n')
        target1 =str(input("first :"))
        target2 =str(input("second :"))

        res = sim(target1,target2)
        print("sim : ")
        print(res)
    elif inpot==4:
        print('\n')
        ta =str(input("first :"))
        recomandation(ta)
        

    
    
    
     
    
                    
#     # if len(Mfile)==59:
#     #     for item in Mfile:
#     # print(Mfile,'\n')
        
    

