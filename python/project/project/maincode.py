import os
import numpy as np
import math
os.system('cls')
print("**************************************Welcom to Movie recommendation system (made by p.hsah)***************************************")
print('\n')
# print('\n')
print("0 : Back to Menu")
print('\n')
print("1 : Movie list")
print('\n')
print("2 : Ratings list")
print('\n')
print("3 : Similarity between tow users")
print('\n')
print("4 : Movie recommendation")
print('\n')
print("5 : Rate a Movie")
print('\n')
print("6 : Add a Movie")
print('\n')
print("7 : Remove a Movie")
print('\n')

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
                
                # print(srow)
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
      
def finenibor(target):
    x=[]
    y=[]
    for i in range(51 ):
        # print(i)
        # print(target)
        z= sim(str(target),str(i))
        # print(y)
        x.append((z,i))
    x.sort(reverse=True)
    # print(x)
    # print("x : ",x[1])
    s,u=x[1]
    s1,u1=x[2]
    s2,u2=x[3]
    s3,u3=x[4]
    s4,u4=x[5]
    s5,u5=x[6]
    s6,u6=x[7]
    s7,u7=x[8]
    
    y.append(u)
    y.append(u1)
    y.append(u2)
    y.append(u3)
    y.append(u4)
    y.append(u5)
    y.append(u6)
    y.append(u7)
    y.append(s)
    y.append(s1)
    y.append(s2)
    y.append(s3)
    y.append(s4)
    y.append(s5)
    y.append(s6)
    y.append(s7)
    return y;
# this is my algorithem for recomedation/////////////////////////////////////////////////////////////////////////////////////
    # print("u",u)
    
    # Rating_file = open('Ratings.txt')
    # readR = Rating_file.readlines()
    # ranked =[]
    # ranked2 =[]
    # # sim=np.array
    # counter=0
    # multi=0
    # x=0
    # rec=[]
    # # print(readR)1
    # for item in readR:
        
    #     part = item.strip().split('\t')
    #     # print(part[0])
    #     if part[0]==target:
    #         # print("okay")
    #         ranked.append([int(part[1]),int(part[2])])
    #     if part[0]==str(u):
    #         # print("okay")
    #         ranked2.append([int(part[1]),int(part[2])])
    # f_matrix=np.array(ranked)
    # s_matrix=np.array(ranked2)
    # # frow=f_matrix[:,0]
    # # frrow=f_matrix[:,1]
    # # print(f_matrix)
    # # print(s_matrix)
    
    # for i in range(s_matrix.shape[0]):
    #     srow = s_matrix[i][0]
    #     srrow = s_matrix[i][1]
    #     multi = 0
    #     found = False
    #     for j in range(f_matrix.shape[0]):
    #         if srow == f_matrix[j][0]:
    #             found = True
    #             break
    #     if not found:
    #         rec.append((srow, srrow))

                
    # rec.sort(key=lambda x: x[1], reverse=True) 
    # # print("rec",rec)
    # movie_file = open('movies.txt')
    # readM = movie_file.readlines()
    # for i in range(3):
    #     # print("recomendation : " ,rec[i][0])
    #     print("**********Recomandations********************************************************************")  
    #     for item in readM:
    #         partt= item.strip().split('\t')
    #         # print(part[0])
    #         if partt[0]==str(rec[i][0]):
                
    #             print(" Film : ",partt[1],'\t',partt[2],'\n')
    #this is my recamndatioin algorithem//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
         
def recomendatin(target):
    
    Rating_file = open('Ratings.txt')
    readR = Rating_file.readlines()
    rec=[]
    y=finenibor(target)
    result=[]
    for i in range(7):
        g=0

        j=0
        ranked =[]
        ranked2 =[]
        # sim=np.array
        counter=0
        multi=0
        x=0
        # print(readR)1
        for item in readR:
            
            part = item.strip().split('\t')
            # print(part[0])
            if part[0]==target:
                # print("okay")
                ranked.append([int(part[1]),int(part[2])])
            if part[0]==str(y[i]):
                # print("okay")
                ranked2.append([int(part[1]),int(part[2])])
        f_matrix=np.array(ranked)
        s_matrix=np.array(ranked2)
        g=y[i]
        kk=y[i+8]
        # print(j)
        # frow=f_matrix[:,0]
        # frrow=f_matrix[:,1]
        # print(f_matrix)
        # print(s_matrix)
        
        for i in range(s_matrix.shape[0]):
            srow = s_matrix[i][0]
            srrow = s_matrix[i][1]
            
            found = False
            for j in range(f_matrix.shape[0]):
                if srow == f_matrix[j][0]:
                    found = True
                    break
            if not found:
                already_in_rec = False
                for r in rec:
                    if r[0] == srow:
                        already_in_rec = True
                        break
                if not already_in_rec:
                    rec.append((srow, srrow, g, kk))
            # rec.append((srow, srrow,g,kk))
                #print("hgelllldslfj")
    # print(rec)
    # print("lllllllllllllll",rec)
    for i in range(1,len(rec)):
        s2=0
        p=0
        h=0
        hu=0
        res=0
        for j in range(len(rec)):     
            if rec[i][0]==rec[j][0]:
                h=rec[i][1]*rec[i][3]  
                hu=rec[j][1]*rec[j][3]
                s=rec[i][3]+rec[j][3]
                p+=h+hu
                s2+=s
        
            if s2>0:
                res=p/math.sqrt(s2)
                if res>0:
                    result.append((str(res),str(rec[i][0])))
    
    fres=[]
    helper=[]
    for item in result:
        ress,ii=item
        if ress not in helper:
            fres.append((str(ress),ii))
            helper.append(ress)
        
    fres.sort(key=lambda x: x[0], reverse=True) 
       
    movie_file = open('movies.txt')
    readM = movie_file.readlines()
    
    print("**********Recomandations********************************************************************")  
    for i in range(3):
        print("recomendation : " ,fres[i][1])
        for item in readM:
            partt= item.strip().split('\t')
            # print(part[0])
            if partt[0]==str(fres[i][1]):
                
                print(" Film : ",partt[1],'\t',partt[2],'\n')
 
def addmovie(movieid,Moviename,year):
    M_file = open('Movies.txt')
    readR = M_file.readlines()
    if year>2025:
        print("Did you time travle ?")
        return
    if int(movieid)<60:
        print("Error")
        return
    print("added")
    
        
    
    add=str(Moviename)+'\t'+str( year)
    Mm_file = open('Movies.txt','a')
    for line in readR:
        parts =line.strip().split('\t')
        if parts[1] == str( Moviename):
            print("ERROR movie name not valid")
            return;
    else:
        Mm_file.write('\n'+str(movieid)+'\t'+str(Moviename)+'\t'+str( year)+'\n')
        
def addacoment(id,mid,rate):
    Rating_file = open('Ratings.txt','r')
    readR = Rating_file.readlines()
    M_file = open('Ratings.txt')
    readM = Rating_file.readlines()
    
    M_file = open('Movies.txt', 'r')
    readM = M_file.readlines()
    max_mid = 0
    for line in readM:
        parts = line.strip().split('\t')
        if int(parts[0]) > max_mid:
            max_mid = int(parts[0])

    if mid > max_mid:
        print("ERROR movie id too big")
        return
    if rate>5:
        print("ERROR betwwen 1 to 5")
        return;
    if id<50 or id>1000:
        print("ERROR ")
        return
    print("added")
    
        
    
    add=str(id)+'\t'+str(mid)+'\t'+str(rate)
    Rr_file = open('Ratings.txt','a')
    for line in readR:
        parts =line.strip().split('\t')
        if parts[0] == str(id) and parts[1]==str(mid):
            print("ERROR rate has been used")
            return;
    else:
        Rr_file.write('\n'+str(id) +'\t'+ str(mid) +'\t'+str(rate)+'\n')
        
def removeamovie(id):
    M_file = open('Movies.txt')
    readR = M_file.readlines()
    Mmfile = open('Movies.txt','w')
    # readR = M_file.readlines()
    if id>2025:
        print("Did you time travle ?")
        return
    
    
        
    
    # add=str(Moviename)+'\t'+str( year)
    for line in readR:
        parts =line.strip().split('\t')
        if parts[0] != str( id):
            Mmfile.write(line)
            
    Mmfile.close()
    print("Removed")
   


while True :
    
                    
    inpot =int(input("Enter your choice :"))

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
        print("**************************************Welcom to Movie recommendation system (made by p.hsah)***************************************")
        print('\n')
        print('\n')
        print("0 : Back to Menu")
        print('\n')
        print("1 : Movie list")
        print('\n')
        print("2 : Ratings list")
        print('\n')
        print("3 : Similarity between tow users")
        print('\n')
        print("4 : Movie recommendation")
        print('\n')
        print("5 : Rate a Movie")
        print('\n')
        print("6 : Add a Movie")
        print('\n')
        # inpot =int(input("press what you want to do :"))
    elif inpot==3:
        print('\n')
        os.system('cls')
        target1 =str(input("first :"))
        target2 =str(input("second :"))

        res = sim(target1,target2)
        print("sim : ")
        print(res)
    elif inpot==4:
        print('\n')
        os.system('cls')
        ta =str(input("first :"))
        finenibor(ta)
        recomendatin(ta)
    elif inpot==5:
        print('\n')
        os.system('cls')
        id=int(input("ID :"))
        mid=int(input("Movie : "))
        rate =int(input("rate 1 to 5 : "))
        addacoment(id,mid,rate)
    elif inpot==6:
        print('\n')
        os.system('cls')
        idd=int(input("id :"))
        midd=str(input("name : "))
        rated =int(input("yaer: "))
        addmovie(idd,midd,rated)
    elif inpot==7:
        print('\n')
        os.system('cls')
        iddd=int(input("id :"))
        removeamovie(iddd)
    else:
        print("Error")
        
        

    
    
    
     
    
                    
#     # if len(Mfile)==59:
#     #     for item in Mfile:
#     # print(Mfile,'\n')

# def removeamovie(id):
#     M_file = open('Movies.txt')
#     readR = M_file.readlines()
#     Mmfile = open('Movies.txt','w')
#     # readR = M_file.readlines()
#     if id>2025:
#         print("Did you time travle ?")
#         return
    
    
        
    
#     # add=str(Moviename)+'\t'+str( year)
#     for line in readR:
#         parts =line.strip().split('\t')
#         if parts[0] != str( id):
#             Mmfile.write(line)
            
#     Mmfile.close()
#     print("Removed")
   
        
    

