#Fizz Buzz 
#Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd

def fizz_buzz(num):
    return "FIZZ" if num%2 == 0 else "BUZZ"

print(fizz_buzz(2))
print(fizz_buzz(3))