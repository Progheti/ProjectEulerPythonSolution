# progheti 11/17/2023
# Problem four
# Smallest Multiple
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def main():
    maxDivisionNumber=20                                                            # variable that will be the highest number
    leastCommonMultiple=1                                                           # the smallest value for smallest ,ultiple that two or more numbers have in common
    for firstSpot in range(2,maxDivisionNumber+1):                                  # loop each value from the max amount of number 
        highestCommonFactor=1                                                       # during this loop, create the variable for the HCF
        for secondSpot in range(2,firstSpot+1):                                     # create a nested loop that adds one ahead the first loop
            if firstSpot%secondSpot==0 and leastCommonMultiple%secondSpot==0:       # during this loop, check numbers if the solution has no remainders
                highestCommonFactor=secondSpot                                      # if the values passes then the value of the second loop will be the HCF, if not, keep looping
        leastCommonMultiple=(leastCommonMultiple*firstSpot) / highestCommonFactor   # update the  LCM, then loop line 11-14 again until firstNumber is complete
    print(leastCommonMultiple)                                                      # print the result

main()