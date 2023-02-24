"""
Name: Benjamin Cesero
Date Due: 9/21/22
Course: CSCI 3351
Description: The following code will return all substrings of a parameter in an array.
It will also remove the duplicate parts if needed.
"""


def main():
    substring = input(
        'Please type what you would like a substring for: ')  # Ask user for input and set it = to a variable

    # Uses list comprehension, string slicing, & conditions
    ans = [substring[a: b]
           for a in range(len(substring))
           for b in range(a + 1, len(substring) + 1)]

    print("All substrings of string are: " + str(ans))  # Print answer with duplicates

    while True:
        go = input('Would you like to remove duplicates? Y or N: ')
        if (go == 'Y') or (go == 'y'):  # conditional loop
            ans = [*set(ans)]  # removes duplicates
            print("All substrings of string without duplicates are: " + str(ans))  # Print answer without duplicates
            quit(True)  # quits code
        elif (go == 'N') or (go == 'n'):  # conditional loop
            quit(True)  # quits code


main()  # calls function
