try:
 x = int(input("enter a number:"))
 count = 0
 for i in range(1,x):
        if x%i==0:
            count+=1
 if count<2:
        print("the number is prime.")
 else:
        print("the number is not prime.")
except:
     print("value error")
finally:
     print("the program is done.")
