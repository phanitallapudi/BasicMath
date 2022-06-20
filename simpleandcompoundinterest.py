

def simple(org,ist,tme):                                            #This function is called when simple interest is called upon
    
    return (org*ist*tme)/100


def compound(org,ist,tme):                                          #This function is called when compound interest is called upon
    
    x = 1/ist

    final = org*((1+x)**tme)
    return final

try:
    while True:
        print("\n***********************************\n")            #The inputs of compound or simple interest are stored in the 
        org = int(input("Enter the original amount: "))             #variable defined as 'org' for the original amount
        ist = int(input("Enter the interest amount: "))             #'ist' for the interest percent and 'tme' for the amount to time
        tme = int(input("Enter the time period: "))
        print("\n***********************************\n")
        
        inp = input("Enter").lower()                                #Use 'sim' to calculate simple interest and 'com' for compound interest
        print("\n***********************************\n")
        if inp == 'sim':
            print(simple(org,ist,tme))

        elif inp == 'com':
            print(round(compound(org,ist,tme),3))

        elif inp == 'q':                                            #Last two if statement are used for breaking the loop or 
            quit()                                                  #printing the errors occured in the process
        else:
            print("Unknown input")

except KeyboardInterrupt:
    print("Exited..")
except ValueError:
    print("Only numericals are accepted!!!")