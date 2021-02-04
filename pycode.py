from random import randrange

def bigNum(a):
    inNum = a
    num = 0
    for n in inNum:
        if n > num:
            num = n

    return num

if __name__ == "__main__":
    array = []
    for i in range(randrange(1,11)):
        array.append(randrange(1,101))
    

    print(bigNum(array))
    
    
    
    