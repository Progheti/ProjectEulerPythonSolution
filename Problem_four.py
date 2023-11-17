# progheti 11/16/2023 -> 11/17/2023
# Problem four
# Largest Palindrome Product
# Find the largest palindrome made from the product of two 3-digit number


def main():                                                             #a function that creates new numbers and get result from isPalindrome()
    multipliedNumbers=0                                                 #variable that will be the soution to the two numbers
    firstNumber=100                                                     #make the first number the min value for a 3-digit number
    secondNumber=100                                                    #make the second number also the min value for a 3-digit number
    while firstNumber<=999:                                             #loop the second number until the number reaches 999, the max 3-digit number
        while secondNumber<=999:                                        #loop the second number until the number reaches 999
            if isPalindrome(firstNumber*secondNumber):                   #sends numbers to isPalindrome to check if the number is a palindrome
                if isPalindrome(firstNumber*secondNumber):               #checks again to show the numbers as well as update the multipledNumbers
                    if firstNumber*secondNumber>multipliedNumbers:      #if the number gets bigger it will update the variable
                       multipliedNumbers=firstNumber*secondNumber       #updates variable
                print(firstNumber*secondNumber)                         #prints the palindrome
            secondNumber+=1                                             #this count the first and second number like 100*(100+1...)
        firstNumber+=1                                                  #Once secondNumber reaches 999, it reset the second number and increases the firstNumber 101*(100+1...)
        secondNumber=100                                                #reset second number to 100
    print(multipliedNumbers)                                            #prints the highest number
           




def isPalindrome(givenNumber):                                           #a function that will check if the multiple of the first and second number are palindrome
    givenNumber=str(givenNumber)                                        #changing the data type to string
    palindrome=True                                                     #bloolean variable
    frontHalfNumber=0                                                   #variable that will be the start of the string
    backHalfNumber=-1                                                   #varibale that will be the end of the string
    while frontHalfNumber<len(givenNumber):                             #loops until the front number is as big as the length of the number
        if givenNumber[frontHalfNumber]!=givenNumber[backHalfNumber]:   #if the front number does not equal the the back number, it's not a palindrome
            palindrome=False                                            #change boolean value
        frontHalfNumber=frontHalfNumber+1                               #move to next number
        backHalfNumber=backHalfNumber-1                                 #move to prevoius number
    return palindrome                                                   #return result to main function
main()