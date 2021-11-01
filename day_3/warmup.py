#Fizz Buzz #2
#Write a function to print all numbers 1 to n, but there are some constraints
#If the number is divisible by 3, print 'Fizz' instead of the number
#If the number is divisible 5, print 'Buzz' instead of the number
#If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
#Otherwise, simply print the number

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)



def fizzbuzz2(n):
    print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i, range(1,n+1))))

def fizzbuzz3(n):
    for i in range(1, n+1: 
        print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))

fizzbuzz2(15)
