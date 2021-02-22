

list1 = [i for i in range(1, 101) if i % 2 == 0 and i % 3 == 0]



def cosPro(n,p):
    return n if n > p else p

if __name__ == "__main__":
    print(cosPro(3, 6))


    print(cosPro(123452461246124.123,12341612342134236123423))

    print(list1)
    print(all(list1))
    print(any(list1))
