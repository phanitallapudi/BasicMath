
def add(x,y):
    return ("Addition of {} and {} is".format(x,y),x+y)                  #Defining multiplication using functions
def sub(x,y):
    return ("Subtraction of {} and {} is".format(x,y),x-y)                  #Defining multiplication using functions
def mul(x,y):
    return ("Multiplication of {} and {} is".format(x,y),x*y)                  #Defining multiplication using functions
def div(x,y):
    return ("Division of {} and {} is".format(x,y),x/y)                  #Defining multiplication using functions
def percent(x,y):
    return ("Percentage of {} to {} is".format(x,y),x%y)                  #Defining multiplication using functions

rct = ['','','','','']                                                      #for the history, it will be only consisting of last 5 values
print("\nThe keys for the operations are:\n\n->History        = 'his'\n->For help       = 'help'\n->Addition       = '+'\n->Substraction   = '-'\n->Multiplication = '*'\n->Division       = '/'\n")
try:
    while True:
        sym = input("Enter the symbol for operation: ")                  #taking input and symbols from the user so we can proceed with the program
        if sym == '+' or sym == '-' or sym == '*' or sym == '/':
            n1 = int(input("Enter number 1                : "))
            n2 = int(input("Enter number 2                : "))

            if sym == '+':
                del rct[0]
                rct.append(add(n1,n2))
                print(add(n1,n2))
            elif sym == '-':
                del rct[0]
                rct.append(sub(n1,n2))
                print(sub(n1,n2))
            elif sym == '*':
                del rct[0]
                rct.append(mul(n1,n2))
                print(mul(n1,n2))
            elif sym == '/':
                del rct[0]
                rct.append(div(n1,n2))
                print(div(n1,n2))
            elif sym == '%':
                del rct[0]
                rct.append(percent(n1,n2))
                print(percent(n1,n2))
            
            

            else:
                break
        elif sym == 'his' or sym == 'HIS':
            print(rct)                  #this print functions gives the history upto the last five calculations
        elif sym == 'help' or sym == 'HELP':
            print("\nThe keys for the operations are:\n\n->History        = 'his'\n->For help       = 'help'\n->Addition       = '+'\n->Substraction   = '-'\n->Multiplication = '*'\n->Division       = '/'\n")
        else:
            print("Invalid keystrokes")
            break
except KeyboardInterrupt:
    print("{NILL}\nExited successfully")

except ZeroDivisionError:
    print("Cannot solve, division by zero")




