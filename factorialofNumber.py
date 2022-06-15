f = True
while f:#Creating a loop so that user can choose whether to go through the program one more time or exit
    x = int(input("User : "))
    #Getting the number to get the factorial
    r = x

    if x == 1 or x ==2:     #If the given input is either 1 or 2, then it will return the same input value
        print("The factorial of {} is {}".format(x,x))
    else:
        if x < 0:
                print("Negative number")
        elif x == 0:
                print("Factorial of 0 is 1")
        else:
            while r<=x:
                for i in range(1,x):
                        r = r*i     #Getting the factorial of the number n using this logic
            print(r)

    print("**********************************")

    nowr = input("Enter Y to get factiorial of another number or N to exit (Y/N): ").lower()    
                                    #Giving a chance to the user whether to exit or replay the code again without running it again
    if nowr == 'y':
        f = True
    elif nowr == 'n':
        print("\ndone!!!")
        f = False
    else:
        print("\nUnknown type")
        print("**********************************")

        


