X, Y, N = map(int, input().split())

def fizzbuzz(number):
    if number % X == 0:
        if number % Y == 0:
            print("FizzBuzz")
            return
        print("Fizz")
    elif number % Y == 0:
        print("Buzz")
    elif number % X != 0 and number % Y != 0:
        print(number)
    return
    
for x in range(1, N+1, 1):
    fizzbuzz(x)
