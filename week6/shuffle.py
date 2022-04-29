# Import required module
import random
 
def shuffle(nArr):
    # check if list is empty
    if len(nArr) < 2:
        return nArr
     
    for pos in range(len(nArr)):
        temp = nArr[pos]
        randPos = random.randint(0, len(nArr)-1)
        nArr[pos] = nArr[randPos]
        nArr[randPos] = temp

    return nArr
        

# Assign array
arr = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(arr)
print(shuffle(arr))
print(shuffle(arr))
print(shuffle(arr))
print(shuffle(arr))
print(shuffle(arr))
print(shuffle(arr))