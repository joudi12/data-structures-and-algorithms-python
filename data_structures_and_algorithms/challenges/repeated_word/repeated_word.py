import re
def find_world(string):
    x = re.sub("," , "", string)
    arr=x.split(' ')
    print (arr)
    output=[]
    for  i in arr:#o(n)
        i= i.lower()
        if i in output :#o(n)
            return i
        else:
            output.append(i)

