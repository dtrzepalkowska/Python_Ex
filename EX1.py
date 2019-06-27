def Ex1():
    print('-----------EXERCISE 1-----------')
    str1="79-900"
    str2="80-155"

    num1=int(str1[:2]+str1[3:])
    num2=int(str2[:2]+str2[3:])

    print('List of post-codes:')

    for x in range(num1,num2):
        elem =str(x+1)
        print(elem[:2]+"-"+elem[2:])
    print('--------------------------------')

def Ex2():
    print('-----------EXERCISE 2-----------')
    print('Generate a list of numbers from 1 to n. Please input n:')
    x = int(input())
    arr = []

    for i in range(0,x):
        arr.append(i+1)

    print('Please input some numbers in range 1-n, separated by a coma')
    numbers = input()
    arr_input = numbers.split(",")
    arr_input = [ int(y) for y in arr_input ]
    arr_input.sort()

    missing_numbers = []

    for number in arr:
        if number not in arr_input:
            missing_numbers.append(number)

    print("Here are the missing numbers: ")
    print(missing_numbers)
    print('--------------------------------')

def Ex3():
    print('-----------EXERCISE 3-----------')
    arr = []
    arr_2 = []
    start = 2
    end = 6

    for x in range (start*10,end*10,5):
        arr.append(x)
    for i in arr:
        arr_2.append(i/10)
    print('List of numbers from 2 to 5.5:')
    print(arr_2)
    print('--------------------------------')

Ex1()
Ex2()
Ex3()