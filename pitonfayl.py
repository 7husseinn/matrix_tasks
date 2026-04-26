#1a
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(-10,10)
    return a
def cem(a):
    s=0
    for i in a:
        for j in i:
            s=s+abs(j)
    return s
n,m=map(int,input("setir ve sutunu daxil edin: ").split())
a=my_matrix(n,m)
for i in a:
    for j in i:
        print(f"{j:4}",end="")
    print()
print(cem(a))"""
#1b
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    b=hasil(a)
    return b
def hasil(a):
    prdct=1
    for i in a:
        for j in i:
            prdct*=j**2
    return prdct            
n,m=map(int,input("setir ve sutunu daxil edin: ").split())
print(my_matrix(n,m))"""
#1c
"""def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a
def k_setri(a,k):
    prdct=1
    setir=1
    for i in a:
        if setir==k:
            for j in i:
                prdct=prdct*j
        setir+=1
    return prdct
n,m=map(int,input("setir ve sutunu daxil edin: ").split())
k=int(input("setiri daxil edin: "))
a=my_matrix(n,m)
print(k_setri(a,k))"""
#1e
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a
def matrix_dia(a):
    sol_dia=[]
    sag_dia=[]
    cem1=0
    cem2=0
    for i in range(n):
        for j in range(m):
            if j==i:
                sol_dia+=[a[i][j]]
            elif j+i==n-1:
                sag_dia+=[a[i][j]]
    for i in sol_dia:
        cem1+=i
    for i in sag_dia:
        cem2+=i
    if cem1>cem2:
        return 0
    elif cem1==cem2:
        return 1
    else:
        return 2
n,m=map(int,input("setir ve sutunu daxil edin: ").split())
a=my_matrix(n,m)
if matrix_dia(a)==0:
    print("sol dia sagdan boyukdur")
elif matrix_dia==1:
    print("sag dia soldan boyukdur")
else:
    print("her iki dia beraberdir")"""
#2a
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return(a)
def cem_ferq(a,b):
    c=[]
    for i in range(n):
        for j in range(n):
                c=c+[[a[i][j]+b[i][j],a[i][j]-b[i][j]]]
    return c                
n=int(input("setir ve sutunu daxil edin: "))
a=my_matrix(n)
b=my_matrix(n)                     
c=cem_ferq(a,b)
print(c)"""
#2b
"""import random
def my_matrix(n):
    k=int(input("setri daxil edin: "))
    m=int(input("sutunu daxil edin: "))
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    b=[]
    for i in range(n):
        b=b+[[0]*n]
        for j in range(n):
            b[i][j]=random.randint(-10,10)
    for i in b:
        for j in i:
            print(f"{j:4}",end="")
        print()
    c=hasil(a,b,k,m)
    return c
def hasil(a,b,k,m):
    c=[]
    prdct=1
    for i in range(n):
        prdct*=a[k-1][i]
    c=c+[prdct]
    prdct=1
    for i in range(n):
        prdct*=b[i][m-1]
    c=c+[prdct]
    return c
n=int(input("setri ve sutunu daxil edin: "))
print(my_matrix(n))"""
#3c
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,100)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    k=pronic(a)
    return k
def pronic(a):
    b=[]
    for i in range(n):
        for j in range(1,n,2):
            z=False
            k=a[i][j]
            for t in range(1,k//2):
                if k==t*(t+1):
                    z=True
            if z:
                b=b+[k]
            z=False
    return b
n=int(input("setir sayini daxil edin: "))
print(my_matrix(n))"""
#3d
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    c=dia(a,n)
    return c
def dia(a,n):
    c=[]
    for i in range(n):
        for j in range(n):
            if j+i==n-1 or i==j:
                t=True
                k=a[i][j]
                for z in range(2,int(k**0.5)+1):
                    if k%z==0:
                        t=False
                if t and k!=1:
                    c=c+[k]
                t=True
    return c
n=int(input("setir ve sutun sayini daxil edin: "))
print(my_matrix(n))"""
#4b
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,99)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    a=dia_yuxari(a,n)
    return a
def dia_yuxari(a,n):
    for i in range(n):
        for j in range(n):
            if j>=i:
                if a[i][j]>=50:
                    a[i][j]=255
                else:
                    a[i][j]=0
    print()
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a
n=int(input("setir ve sutun sayini daxil edin: "))
my_matrix(n)"""
#4d
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,99)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    print()
    for i in range(n):
        for j in range(n-1,-1,-1):
            print(f"{a[i][j]:4}",end="")
        print()
n=int(input("setir ve sutun sayini daxil edin: "))
my_matrix(n)"""            
#4e
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,99)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    print()
    for i in range(n-1,-1,-1):
        for j in range(n):
            print(f"{a[i][j]:4}",end="")
        print()
n=int(input("setir ve sutun sayini daxil edin: "))
my_matrix(n)"""
#4f
"""import random
def my_matrix(n):
    a=[]
    b=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,99)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    print()
    for i in range(n):
        b=b+[[0]*n]
        for j in range(n):
            b[i][j]=random.randint(10,99)
    for i in range(n):
        for j in range(n):
            b[j][n-i-1]=a[i][j]
    for i in b:
        for j in i:
            print(f"{j:4}",end="")
        print()    
n=int(input("setir ve sutun sayini daxil edin: "))
my_matrix(n)"""
#5
"""import random
def my_matrix(n):
    a=[]
    for i in range(n):
        a=a+[[0]*n]
        for j in range(n):
            a[i][j]=random.randint(10,99)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    print()
    for i in range(n):
        for j in range(n):
            #1
            """if j==0 or j==n-1 or j==i:
                a[i][j]="+" """
            #2
            """if j==0 or j==n-1 or i==0 or i==n//2:
                a[i][j]="+" """
            #3
            """if ((i==j or i+j==n-1) and i<=n//2) or j==n//2 :
                a[i][j]="+" """
            #4
            """if j==n//2 or i==0:
                a[i][j]="+" """
            #5
            """if i==0 or i==n-1 or i+j==n-1:
                a[i][j]="+" """
            #6
            """if i==0 or j==0 or i==n-1 or j==n-1:
                a[i][j]="+" """                
    for i in a:
        for j in i:
            print(f"{j:2}",end="")
        print()
n=int(input("setir ve sutun sayini daxil edin: "))
my_matrix(n)"""
    
    




    
                    

            
    
                    
                    
                    
        
    
    
        
        
    



    


        
                



            
        
            
            
        

