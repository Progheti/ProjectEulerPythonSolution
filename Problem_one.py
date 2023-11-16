# progheti 11/16/2023
# Problem 1
# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5
# We get 3,5,6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# create a function
def main():
#set a variable that will be used to multiple 3 or 5
    numberCheck=0
#create a loop that goes through a range of 1-1000
    for each in range(1,1000):
# a decision to check if the remainder of the check numbers are zero
        if each%3==0 or each%5==0:
#if it is zero then that means the number is evenly divisible by 3 or 5
# add each to numbercheck and update numbercheck to the total from each 
            numberCheck+=each
#Once done with the loop, display the sum of all multiples
    print(numberCheck)

        





#call the function
main()