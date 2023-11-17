# progeti 11/16/2023
# Problem 3
# Largest Prime Factor
# What is the largest prime factor of the number 600851475143?

def main():                                    #a function
    largestNumber=600851475143                 #the value of the highest number wanted
    prime=2                                    #instead of multipling until we get to
    while prime<=largestNumber:                #loop until the prime variable is less or equal to
        if(largestNumber%prime==0):            #decision to check if the equation has no remainders.
            largestNumber=largestNumber/prime  #if it does not have any remainder, update variable to the solution to the equation
        else:
            prime=prime+1                      #update prime number if the check does have remainders
    print(prime)                               #Once the loop ends display result
main()