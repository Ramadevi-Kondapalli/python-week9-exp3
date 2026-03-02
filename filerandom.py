import random
f=open("random_numbers.txt","w")
for i in range(20):
    num=random.randint(1,100)
    f.write(str(num)+"\n")
f.close()
print("20 random numbers written to random_numbers.txt")
f.close()
f=open("random_numbers.txt","r")
print(f.read())
f.close()


    