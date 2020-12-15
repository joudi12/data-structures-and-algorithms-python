
def multi_bracket_validation(input):
    open = ["[","{","("]
    close = ["]","}",")"]
    check = []
    for i in input:
        if i in open:
            check.append(i)
        elif i in close:
            loc = close.index(i)
            if ((len(check) > 0) and (open[loc] == check[len(check)-1])):
                check.pop()
            else:
                return False
    if len(check) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    string = "{(})"
    print(string,"-", multi_bracket_validation(string))
    string = "{}{Code}[Fellows](())"
    print(string,"-",multi_bracket_validation(string))
