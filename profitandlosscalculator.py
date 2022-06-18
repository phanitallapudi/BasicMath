
def profit():
    x = (percent/100)*cost_price                                                    #Profit function calls if the first character in the
    x = cost_price + x                                                              #variable 'start' is '+'
    return x
def loss():
    x = (percent/100)*cost_price                                                    #Loss function calls if the first character in the
    x = cost_price - x                                                              #variable 'start' is '-'
    return x

try:
    f = True
    while f:
        print("\n*********************************\n")
        cost_price = int(input("Enter the MRP of the item: "))                      #Here the cost_price is the mrp of the item.
        start = str(input("Enter the value as +Number/-Number i.e.., (+6): "))      #For the input the first is described as profit/loss i.e..,
                                                                                    #if the symbol is '+' then it will assume it as profit and 
                                                                                    #find the profit and vice versa for '-'
                                                                                    #After the symbols the numericals is the percent for 
                                                                                    #calculating the profit/loss
        print("\n*********************************\n")
        sym = start[0]
        percent = int(start[1:])

        percent = int(percent)

        if sym == '+':
            print("The selling price is",profit())
        elif sym == '-':
            print("The selling price is",loss())

        else:
            print("Invalid operator")
            f = False
    
except KeyboardInterrupt as k:
    print("\nExited after ")
except ValueError as v:
    print("\n",v)



