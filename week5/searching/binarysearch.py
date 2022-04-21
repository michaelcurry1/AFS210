def isInList(olist, item):
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return isInList(olist[:midpoint], item)
            else:
                return isInList(olist[midpoint+1:], item)

        
def binarySearch(alist, item):
    first = 0
    last = len(alist) -1

    while first <= last:
        midpoint = (first + last)// 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                last = midpoint +1
    return False

print(isInList([7, 20, 26, 31, 40, 51, 55, 63, 74, 81], 31))
print(isInList([7, 20, 26, 31, 40, 51, 55, 63, 74, 81], 77))
print(isInList(["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"],  "Delta"))