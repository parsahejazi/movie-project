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
    frow=f_matrix[:,0]
    frrow=f_matrix[:,1]
    
    for i in range(s_matrix.shape[0]):
        srow=s_matrix[i][0]
        srrow=s_matrix[i][1]
        multi=0
        if srow in frow:
            counter+=1
            multi=srrow*frrow
            x+=multi
            print(srow)
            
    return counter
       #dsfdsfdsfdsfdsf     
    
            
        
    

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

        counter = sim(target1,target2)
        print("sim : ")
        print(counter)
        
        

    
    
    
     
    
                    
#     # if len(Mfile)==59:
#     #     for item in Mfile:
#     # print(Mfile,'\n')
        
    

