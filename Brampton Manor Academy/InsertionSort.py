import random
import time

def InsertionSort(nlist):

    start = time.time()

    for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

    print(nlist)

    end = time.time()
    TimeElapsed = end - start
    print(TimeElapsed)

if __name__=='__main__':
    List = []
    Size = int(input("Enter size of list: "))
    for i in range(0,Size):
        Num = random.randint(1,100)
        List.append(Num)
    InsertionSort(List)
