"""functions for printinig prime numbers from 1 to 100"""
def prime():
    """ list to store prime numbers"""
    primelist = []
    """outer loop for looping through our numbers"""
    for j in range(1, 101):
        count =0    
        for i in range(1, j+1):
            if j%i == 0:
                count = count +1
        if (count ==2):           #prime num have only 2 factors
            primelist.append(str(j))
        """else:
            nonprimelist.append(str(j))"""

    print("The list of prime numbers are:"+'\n', primelist)
    #print("The list of non-prime numbers are:" +'\n', nonprimelist)


"""---functions to check string if palindrome or not---"""



def palindrome(userinput):
    """printing the input from user"""
    print("The user input is:", userinput)
    """rerversing the string"""
    inpt = userinput[::-1]
    print("The reversed string is:",inpt)

    """ check if the reversed string matches the input string or not""" 
    if inpt!=userinput:
        print("{}is not a palindrome string".format(str(userinput)))
    else:
        print("{} is a palindrome string".format(str(userinput)))

""""""
def harmonic_series(inp):
    """set counter to store sum"""
    s = 0
    for i in range(1,inp+1):
        s =s+(1/i)
        if i!=0:
            """to print harmonic series"""
            print("1/{} + ".format(i), end = " ")
            """ to print harmonic series sum"""
    print("\nThe sum of series is",round(s,3))



"""--MAIN FUNCTION---"""
if __name__ == '__main__':
    print("---------PRINTING PRIME NUMBERS ONLY FROM 1 TO 100----------")
    prime()
    print('\n')
    print("---------CHECKING WHETHER THE STRING IS PALINDROME OR NOT----------")
    inpt_str = input("Enter the strings:")
    palindrome(inpt_str)
    print('\n')
    print("---------PRINTING HARMONIC SERIES AND ITS SUM---------")
    userinp = int(input("Enter the number of terms: "))
    harmonic_series(userinp)