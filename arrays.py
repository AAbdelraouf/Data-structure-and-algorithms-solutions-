# Arrays #
# from array import *

# array1 = array('i', [10,20,30,40,50])
# array1.insert(-1, 100)
# array1.remove(10)
# for x in array1:
#     print(x)

# Lists #
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print( "list1[0]: ", list1[0])
# print( "list2[1 to 5]: ", list2[1:5])

# del list1[0]
# print(list1)

# listx = ['1','2','3','4',"5"]
# enumerateThis = enumerate(listx)
# print(list(enumerateThis))



def list_of_primes(n):
    primes = []
    for y in range (2, n):
        for z in range(2, y):
            if y % z == 0:
                break
        else:
            primes.append(y)
            primes.sort()
    return primes

print(list_of_primes(100))



