
name="ashwani"
name2=name[::-1]
if name==name2:
    print("equal")
else:
    print("not equal")
    
List=[1,2,3,4,5,6,7,8,9]
if List[0]==1:
    print("one")
    if List[1]==2:
        print("two")
        if List[2]==3:
            print("three")
            if List[3]==4:
                print("four")
                if List[4]==5:
                    print("this is five")
 


n=10
for n in range (10):
    print(n)


for n in range(10):
    if n==4:
        break
    print (n)


List=[1,2,3,4,5,6,7,8,9]
if List[0]==4:  
    print ("one")  
elif List[1]==6:  
     print ("two")  
elif List[2]==1:
    print ("three")
elif List[3]==1:
    print ("four")  
elif List[4]==5:
    print ("five")  


#continue
    for n in range(1,10):
            if n==6:
                continue
            print(n)
