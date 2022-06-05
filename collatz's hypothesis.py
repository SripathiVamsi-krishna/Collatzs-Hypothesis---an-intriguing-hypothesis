c0 = int(input("Enter a non-zero and non-negative number: "))
count = 0
while (c0 > 1):
    if (c0 % 2 == 0):
        c0 = c0 / 2
        print(c0)
        count = count + 1
        #print("The total no.of steps:", count)
    elif (c0 % 2 != 0):
        c0 = ((3 * c0) + 1)
        print(c0)
        count = count + 1
        #print("The total no.of steps:", count)
    elif (c0 == 1):
        count = 1
        #print("The total no.of steps:", count)
        break
    else:
        print("Please enter a valid positive and non-zero number...:(((")
print("The total steps count is ", count)
        