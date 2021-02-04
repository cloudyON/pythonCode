from random import randrange #난수 생성

def bigNum(a): #제일 큰 수를 찾는다
    inNum = a
    num = 0
    for n in inNum:
        if n > num:
            num = n

    return num

if __name__ == "__main__": #시작
    array = []
    for i in range(randrange(1,11)): 
        array.append(randrange(1,101)) #난수 범위 정하기
    

    print(bigNum(array))
    
    
    
    