# chechFile():
# parameter - filename: string
# return value - boolean(flag): depending whether the file can be opened or not
def checkFile(filename):
    try:
        open(filename)
        return True
    except:
        return False

# chechInt():
# parameter - value: string
# return values - value: int, boolean(flag): depending whether the given value can be converted into int or not
def checkInt(value):
    try:
        return int(value), True
    except ValueError:
        return None, False
# main():
# display the menu and takes the input of choice untill user exits
def main():
    print("Hello! Welcome to the file processor.\n")
    menuF = ('Selection Menu: \n 0. Exit Program \n 1. Read from a file \n 2. Write integer to a file \n 3. Append integer to a file\n')
    # loop untill user exits
    while True:
        # displaying the menu
        print('Selecttion Menu:')
        print('0. Exit Program')
        print('1. Read from a file')
        print('2. Write integer to a file')
        print('3. Append integer to a file\n')
        # variable to store the choice
        choice = int(input('What would you like to do? '))

        # if choice == 0 evalutes to be true,
        # user exits from the program
        if choice == 0:
            break

        # if choice == 1 evalutes to be true,
        # file name is taken as input and read operation is performed, if possible
        elif choice == 1:
            # taking file name as input
            filename = input('\nPlease enter in a file name: ')
            # checking if file exists
            if checkFile(filename):
                print('\nReading...\nThe file you entered in contains:\n')
                # opening file in read mode
                file_handler = open(filename, 'r')
                #writing to the file
                print(file_handler.read())
            # if file name is not valid, ie file doesn't exists
            else:
                print('\nSorry, that wasn\'t a valid file. Please try again.\n')
        # if choice == 2 evalutes to be true,
        # file name is taken as input and write operation is performed,
        # if file already exists, then previous content is truncated (or overwritten)
        # Note: No need to check files existence
        elif choice == 2:
            # taking file name as input
            filename = input('\nPlease enter the file you\'d like to write to: ')
            print('\nEnter in the number. Type "done" when you no longer wish to.\n')

            # opening file in write mode
            file_handler = open(filename, 'w')
            # taking new value to be appended untill user enters 'done'
            while True:
                number = input('Enter in a number: ')
                # if 'done' is given as input, loop is 'breaked'
                if number=='done':
                    break
                # checking if 'number' contains an integer
                number, flag = checkInt(number)
                # if number is an integer, ie flag is true, then it is written in the file
                if flag == True:
                    file_handler.write(str(number)+'\n')
                # otherwise prompt is displayed
                else:
                    print('\nThat\'s not an integer! Please try again.\n')
        # if choice == 3 evalutes to be true,
        # file name is taken as input and append operation is performed
        # if file already exists, then previous content is not truncated, rather new content is 'added' at the end
        elif choice == 3:
            # taking file name as input
            filename = input('\nPlease enter the file you\'d like to append to: ')
            # checking if file exists
            if checkFile(filename):
                print('\nEnter in the number. Type "done" when you no longer wish to.\n')
                # opening file in write mode
                file_handler = open(filename, 'a')
                # taking new value to be appended untill user enters 'done'
        while True:
            number = input('Enter in a number: ')
            # if 'done' is given as input, loop is 'breaked'
            if number=='done':
                break
            number, flag = checkInt(number)
            # if number is an integer, ie flag is true, then it is written in the file
            if flag == True:
                file_handler.write(str(number)+'\n')
            # otherwise prompt is displayed
            else:
                print('\nThat\'s not an integer! Please try again.\n')
        # if file name is not valid, ie file doesn't exists
        else:
            print('\nSorry, that wasn\'t a valid file. Please try again.\n')
    # if the choice is not valid
    else:
        print('\n Please enter a valid choice.\n')

# making call to main()
if __name__ == '__main__':
    main()