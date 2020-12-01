
def array_binary_search (val,my_list):
    found = False
    first = 0
    last = len(my_list)-1
    while first <=last and found == False :
        middel=(first+last)//2
        if my_list[middel]==val :
            found =True
            return middel
        else:
            if my_list[middel]< val :
                first =  middel+1
            else :
                last = middel-1
    if found != False :
        return middel
    else:
        return -1
# print(array_binary_search(4,[2,3,4,6,7,8,15,16,17]))
