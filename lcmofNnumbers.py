
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)    #recursive implementation until the if statement passes and returns b as a value for the lcm function
def lcm(arr, idx):
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = lcm(arr, idx+1)
    return int(a*b/gcd(a,b))#getting the final output of the given numbers lcm

f = True
while f:
    try:
        numb = int(input("Enter the total number of numbers you want to enter: "))#Getting the total number of numbers from the user

        nums = []

        for _ in range(numb):

            r = int(input("Enter the number: "))#Getting the particular numbers and appending it into the list(nums)
            nums.append(r)
        
        print("The LCM of the list {} is".format(nums),lcm(nums,0))
    except KeyboardInterrupt:
        print("\nDone!")#To exit the while loop using ctrl+C
        f = False


            