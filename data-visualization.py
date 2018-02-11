#!/usr/local/bin/python3
# this script is not compatible with python2

# encoding definition
"""coding=utf-8"""


# import modules
import os
import platform


# determine os system to clear screen
def clear_screen():
    my_os = platform.system()
    if my_os == 'Windows':
        os.system('cls')  # on windows
    else:
        os.system('clear')  # on linux / os x


# user input for table header
clear_screen()
data_title = input('Enter table header title: ')
print('You entered: %s\n' % (data_title))

column_one_header = input('Enter column 1 header title: ')
print('You entered: %s\n' % (column_one_header))

column_two_header = input('Enter column 2 header title: ')
print('You entered: %s\n' % (column_two_header))


# variables declaration and user data input
clear_screen()
data_str = []
data_int = []
separator = ','
user_data = ''

while user_data != 'x':
    user_data = input('Enter a data name and integer value separated by comma (data, value) (x to stop input): ')

    if user_data == '-1':
        break
    elif separator not in user_data:
        print('Error: comma not included.\n')
    elif user_data.count(separator) > 1:
        print('Error: Too many commas in input.\n')
    else:
        data = user_data.split(separator)

        if data[1].strip().isdigit():
            print('Data string: %s' % (data[0]))
            print('Data integer: %d\n' % (int(data[1])))
            data_str.append(data[0].strip())
            data_int.append(int(data[1]))
        else:
            print('Error: Comma not followed by an integer.\n')


# output formatted table
clear_screen()
    # print table header
print('Table:\n')
print(data_title.center(41, ' '))
print('%-20s|%20s' % (column_one_header, column_two_header))
print('-' * 20 + '+' + '-' * 20)

    # print table data rows
i = 0
while i < len(data_str):
    print('%-20s|%20d' % (data_str[i], data_int[i]))
    i += 1


# output formatted histogram
print('\n\nHistogram:\n')
i = 0
while i < len(data_str):
    print('%20s' % (data_str[i]), '*' * data_int[i])
    i += 1
