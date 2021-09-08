primeList = []
def isPowerful(n):
    if n == 1:
        print(n, " is powerful")
        return True
    if n == 0:
        print(n, " is not powerful")
        return False
    for i in range(2,n):
        isPrime(i)
    if checkPowerful(n, primeList) == True:
        return True
    else:
        return False

def isPrime(x):
    for i in range(2,x):
        if ((x%i)==0):
            return False
        else:
            primeList.append(x)
            break
    return primeList

def checkPowerful(y, list):
    for x in list:
        if y % x != 0 or (y % (x**2)) != 0:
            print(y, "is not powerful")
            return False
        else:
            print(y, "is powerful")
            return True

userInput = input("Enter a number!: ")
isPowerful(int(userInput))