# progheti 12/18/2023
# Problem 7
# What is the 10,001st prime number


#This function controls the flow and counting of the prime numbers.
def main():
    number=1
    primeCountNumber=0
    while primeCountNumber <10001:
        number,primeCountNumber=primeCheck(number,primeCountNumber)
    print(number-1)

#This checks if the number is prime or not. This will send two variables back to the main function
def primeCheck(number,primeNumberCount):
    if number > 1:
        for eachNumber in range(2,number):
            if (number%eachNumber)==0:
                number+=1
                return number,primeNumberCount
        number+=1
        primeNumberCount+=1
        return number,primeNumberCount
    else:
        number+=1
        return number,primeNumberCount
main()