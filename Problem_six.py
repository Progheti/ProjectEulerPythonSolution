# progheti 11/20/2023
# Problem 6
# Sum Square Difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


def main():                                             #function that controls the flow of the program
    totalSumOfSquares=sumOfSquares()                    #saves the solution of this function
    totalSquareOfSums=squareOfSum()                     #saves solution
    theDifference=totalSquareOfSums-totalSumOfSquares   #the square of the sum minus sum of the square will be the answer
    print(theDifference)                                #print result


def sumOfSquares():                                     #function to find the sum of the sqaures
    max=100                                             #the max value to calculate
    squareList=[]                                       #this list stores the value of the sqaures
    for eachNumber in range(0,max+1):                   #loop through every value until it reaches 100
        squared=eachNumber*eachNumber                   # As it loops through it will square itself and save the value
        squareList.append(squared)                      #add the squared value into the list
    return sum(squareList)                              # return the sum of the list to the function that calls it


def squareOfSum():                                      #function to find the square of the sums
    holdMyNumbers=[]                                    #a list that holds all numbers until 100
    max=100                                             #max value
    for eachNumber in range(0,max+1):                   #loops zero through one hundred
        holdMyNumbers.append(eachNumber)                #adds each number to the list
    allAddedUp=sum(holdMyNumbers)                       #adds all numbers inside of list
    return allAddedUp*allAddedUp                        #returns the square of the sum of the list


main()