# proghetti 12/20/2023
# Problem 9
# There exists exactly one Pythagorean triplet for which a+b+c=1000 . Find the product abc.


# loops the range from the lowest value to the highest value of C
# loops the range for A
# sets B 
# checks if a** and b** is C**
# prints the results
def main():
    for eachCNumber in range(334,500):
        for eachANumber in range(1, int((1000-eachCNumber)/2)):
            BNumber=(1000-eachCNumber)-eachANumber
            if eachANumber**2+BNumber**2==eachCNumber**2:
                answer=eachANumber*BNumber*eachCNumber
                print(answer)
main()